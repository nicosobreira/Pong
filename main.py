import curses
import time

import utils
from collision import *

from Vector import Vector
from Ball import Ball
from Player import Player
from Window import Window


def convertRgb(rgb) -> int:
    return rgb * 1000 // 255


class Game:
    def __init__(self, stdscr: int) -> None:
        self.stdscr = stdscr

        # Set new color (with rgb)
        if curses.can_change_color():
            curses.init_color(2, # Green
                convertRgb(32),
                convertRgb(227),
                convertRgb(178),
            )
            curses.init_color(3, # Orange
                convertRgb(237),
                convertRgb(171),
                convertRgb(101)
            )
            curses.init_color(4, # Blue
                convertRgb(44),
                convertRgb(203),
                convertRgb(254)
            )
        
        # Color pairs
        if curses.has_colors():
            curses.use_default_colors()
            
            # Color pairs
            curses.init_pair(1, 2, -1)  # Green
            curses.init_pair(2, 3, -1)  # Yellow
            curses.init_pair(3, 4, -1)  # Blue

        curses.noecho()  # Não exibe os inputs
        # curses.cbreak()
        curses.curs_set(0)  # Não mostra o cursor

        curses.set_escdelay(1)  # Pressionar ESC não "pausa" o jogo

        self.stdscr.nodelay(True)  # Se não tiver input o padrão é -1
        self.stdscr.keypad(True)

        # Game
        self.state = True
        self.pause = False

        self.TICKRATE = 50

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

        self.ball = Ball.spawn(self.stdscr, self.board, color=3)

        player_offset_x = 3
        self.player1 = Player(
            self.stdscr,
            KEYS={"up": 119, "down": 115},
            pos=Vector(
                player_offset_x,
                self.board.middle_y - self.ball.size.y * 3
            ),
            size=Vector(
                self.ball.size.x,
                self.ball.size.y * 3
            ),
            ch="%", color=2
        )

        self.player2 = Player(
            self.stdscr,
            KEYS={"up": curses.KEY_UP, "down": curses.KEY_DOWN},
            pos=Vector(
                self.board.right - self.ball.size.x - player_offset_x,
                self.board.middle_y - self.ball.size.y * 3
            ),
            size=Vector(
                self.ball.size.x,
                self.ball.size.y * 3
            ),
            ch="%", color=2
        )

    def input(self) -> None:
        key = self.stdscr.getch()
        if key == self.KEYS["quit"]:
            self.state = False
        key = self.stdscr.getch()
        if key == self.KEYS["pause"]:
            self.pause = not self.pause

    def update(self) -> None:
        self.player1.input(self.board)
        self.player2.input(self.board)
        
        self.ball.update()

        # Colisão bola e jogador 1
        if isCollidingEntityX(self.ball, self.player1):
            self.ball.vel.x *= -1

        # Colisão bola e jogador 2
        if isCollidingEntityX(self.ball, self.player2):
            self.ball.vel.x *= -1

        if ( isCollidingEntityBoardUp(self.ball, self.board) or
             isCollidingEntityBoardDown(self.ball, self.board)):
            self.ball.vel.y *= -1

        if isCollidingEntityBoardLeft(self.ball, self.board):
            self.player1.score += 1
            self.ball.reset(self.board)

        if isCollidingEntityBoardRight(self.ball, self.board):
            self.player2.score += 1
            self.ball.reset(self.board)

    def render(self) -> None:
        self.stdscr.erase()

        utils.drawPanel(
            self.stdscr,
            self.panel,
            self.player1, self.player2, "-", 0
        )

        self.ball.render()
        self.player1.render()
        self.player2.render()

        if self.pause:
            utils.drawPauseMessage(self.stdscr, self.board)

        self.stdscr.refresh()

    def loop(self) -> None:
        while self.state:
            self.input()

            if not self.pause:
                self.update()

            self.render()

            curses.flushinp()  # Faz com que os inputs não se "arrastem"
            curses.napms(self.TICKRATE)


def main(stdscr) -> None:
    game = Game(stdscr)
    game.loop()


if __name__ == "__main__":
    curses.wrapper(main)
