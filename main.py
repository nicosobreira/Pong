import curses
import time

import utils
from collision import *

from Vector import Vector
from Ball import Ball
from Player import Player
from Window import Window


def convertRgb(rgb) -> int:
    """ Converts 255 to 1000 rgb
    """
    return rgb * 1000 // 255


class Game:
    def __init__(self, stdscr) -> None:
        self.stdscr = stdscr

        # Color pairs
        if curses.has_colors():
            curses.use_default_colors()
            
            # Color pairs
            curses.init_pair(1, curses.COLOR_GREEN, -1)  # Green
            curses.init_pair(2, curses.COLOR_YELLOW, -1)  # Yellow
            curses.init_pair(3, curses.COLOR_BLUE, -1)  # Blue

        curses.noecho()  # Não exibe os inputs
        # curses.cbreak()
        curses.curs_set(0)  # Não mostra o cursor

        self.stdscr.nodelay(True)  # Se não tiver input o padrão é -1
        self.stdscr.keypad(True)

        # Game
        self.state = True
        self.pause = False

        self.TICKRATE = 1000 / 60

        self.KEYS = {
            "quit": 113, # q
            "pause": 112 # p
        }

        self.panel = Window(
            left=0,
            right=curses.COLS,
            up=0,
            down=2
        )

        self.board = Window(
            left=self.panel.left,
            right=self.panel.right,
            up=self.panel.down,
            down=curses.LINES
        )

        self.ball = Ball.new(self.stdscr, self.board, color=3)

        player_offset_x = 3
        self.player1 = Player.new(self.stdscr,
            KEYS={"up": 119, "down": 115},
            x=0,
            offset_x=3,
            size_mult_y=3,
            ball=self.ball,
            board=self.board
        )
        
        self.player2 = Player.new(self.stdscr,
            KEYS={"up": curses.KEY_UP, "down": curses.KEY_DOWN},
            x=self.board.right - self.ball.size.x,
            offset_x=-3,
            size_mult_y=3,
            ball=self.ball,
            board=self.board
        )

    def input(self) -> None:
        key = self.stdscr.getch()
        if key == self.KEYS["quit"]:
            self.state = False
        key = self.stdscr.getch()
        if key == self.KEYS["pause"]:
            self.pause = not self.pause

    def update(self) -> None:
        key = self.stdscr.getch()
        self.player1.input(key, self.board)
        key = self.stdscr.getch()
        self.player2.input(key, self.board)
        
        self.ball.update()

        # Colisão bola e jogador 1
        # if isCollidingEntityLeftRight(self.ball, self.player1):
        #     self.ball.vel.x *= -1

        # Colisão bola e jogador 2
        # if isCollidingEntityRightLeft(self.ball, self.player2):
        #     self.ball.vel.x *= -1

        # if (    isCollidingEntityBoardUp(self.ball, self.board) or
        #         isCollidingEntityBoardDown(self.ball, self.board)):
        #     self.ball.vel.y *= -1

        # if isCollidingEntityBoardLeft(self.ball, self.board):
        #     self.player2.score += 1
        #     self.ball.reset(self.board)

        # if isCollidingEntityBoardRight(self.ball, self.board):
        #     self.player1.score += 1
        #     self.ball.reset(self.board)

    def render(self) -> None:
        self.stdscr.erase()

        utils.drawPanel(
            self.stdscr,
            self.panel,
            self.player1, self.player2, "-", 2
        )

        self.ball.render()
        self.player1.render()
        self.player2.render()

        if self.pause:
            utils.drawPauseMessage(self.stdscr, self.board)

        self.stdscr.refresh()

    def loop(self) -> None:
        previous = time.time()
        lag = 0
        while self.state:
            current = time.time()
            elapsed = current - previous
            previous = current
            lag += elapsed

            self.input()

            while lag >= self.TICKRATE:
                # if not self.pause:
                self.update()
                lag -= self.TICKRATE

            self.render()

            # curses.flushinp()  # Faz com que os inputs não se "arrastem"
            # curses.napms(1000 // self.TICKRATE)


def main(stdscr) -> None:
    game = Game(stdscr)
    game.loop()


if __name__ == "__main__":
    curses.wrapper(main)
