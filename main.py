import curses
import time

import utils
from collision import *

from Ball import Ball
from Player import Player
from Window import Window


# TODO Refatorar o código das colisões
#    * A colisão da bola e player usando lógicas diferentes
# TODO Ver se valhe apena criar uma classe "Score" ou uma função

class Game:
    def __init__(self, stdscr) -> None:
        self.stdscr = stdscr

        # Color pairs
        if curses.has_colors():
            curses.use_default_colors()

            # Color pairs
            curses.init_pair(1, curses.COLOR_MAGENTA, -1)
            curses.init_pair(2, curses.COLOR_YELLOW, -1)
            curses.init_pair(3, curses.COLOR_BLUE, -1)

        # curses.noecho()  # Não exibe os inputs
        curses.curs_set(0)  # Não mostra o cursor
        # curses.cbreak()

        self.stdscr.nodelay(True)  # Se não tiver input o padrão é -1
        self.stdscr.keypad(True)

        # Game
        self.state = True
        self.pause = False
        self.pause_message = "PAUSE"

        self.FRAME_TIME = 1000 / 18

        self.KEYS = {
            "quit": 113, # q
            "pause": 112, # p
        }

        self.score = Window(
            left=0,
            right=curses.COLS,
            up=3,
            down=5
        )

        self.board = Window(
            left=self.score.left,
            right=self.score.right,
            up=self.score.down,
            down=curses.LINES
        )

        self.ball = Ball.new(
            scr=self.stdscr,
            sx=1,
            sy=1,
            board=self.board,
            ch="o",
            color=3)

        self.player1 = Player.new(
            scr=self.stdscr,
            KEYS={"up": 119, "down": 115},
            x=self.board.left,
            offset_x=0,
            size_mult_y=5,
            ball=self.ball,
            board=self.board,
            ch="%",
            color=2
        )

        self.player2 = Player.new(
            scr=self.stdscr,
            KEYS={"up": curses.KEY_UP, "down": curses.KEY_DOWN},
            x=self.board.right - self.ball.size.x,
            offset_x=-0,
            size_mult_y=5,
            ball=self.ball,
            board=self.board,
            ch="%",
            color=2
        )
        self.objects = [self.ball, self.player1, self.player2]

    def input(self, key):
        if key == self.KEYS["quit"]:
            self.state = False
        if key == self.KEYS["pause"]:
            self.pause = not self.pause
        self.player1.input(key, self.board)
        self.player2.input(key, self.board)

    def update(self) -> None:
        key = self.stdscr.getch()
        self.input(key)
        self.ball.update()

        # Colisão bola e jogador 1
        if isCollidingEntityLeftRight(self.ball, self.player1):
            self.ball.vel.x *= -1

        # Colisão bola e jogador 2
        if isCollidingEntityRightLeft(self.ball, self.player2):
            self.ball.vel.x *= -1

        if isCollidingEntityBoardUp(self.ball, self.board):
            self.ball.vel.y *= -1

        if isCollidingEntityBoardDown(self.ball, self.board):
            self.ball.vel.y *= -1

        if isCollidingEntityBoardLeft(self.ball, self.board):
            self.player2.score += 1
            self.ball.reset(self.board)

        if isCollidingEntityBoardRight(self.ball, self.board):
            self.player1.score += 1
            self.ball.reset(self.board)

    def render(self):
        self.stdscr.erase()

        utils.drawPanel(
            self.stdscr,
            self.score,
            self.player1,
            self.player2,
            color=1
        )

        objects = sorted(
            self.objects,
            key=lambda obj: obj.pos.x)
        for obj in objects:
            obj.render()

        if self.pause:
            utils.addstr(
                self.stdscr,
                self.board.middle_x - len(self.pause_message),
                self.board.middle_y,
                self.pause_message,
                0
            )

        self.stdscr.refresh()

    def loop(self):
        previous = time.time()
        while self.state:
            current = time.time()
            elapsed = current - previous


            if not self.pause:
                self.update()

            self.render()

            curses.flushinp()  # Faz com que os inputs não se "arrastem"

            if elapsed < self.FRAME_TIME:
                curses.napms(round(self.FRAME_TIME - elapsed))
            previous = time.time()



def main(stdscr):
    game = Game(stdscr)
    game.loop()


if __name__ == "__main__":
    curses.wrapper(main)
