import curses
import time

import utils
import collision as col

from Vector import Vector
from Ball import Ball
from Player import Player


class Game:
    def __init__(self, stdscr) -> None:
        self.stdscr = stdscr

        # Set color
        curses.start_color()
        curses.use_default_colors()

        # curses.cbreak() #
        curses.noecho()  # Não exibe os inputs
        curses.cbreak()
        curses.curs_set(0)  # Não mostra o cursor

        curses.set_escdelay(1)  # Pressionar ESC não "pausa" o jogo

        self.stdscr.nodelay(True)  # Se não tiver input o padrão é -1
        self.stdscr.keypad(True)

        # Color pairs
        curses.init_pair(1, 2, -1)  # Green
        curses.init_pair(2, 3, -1)  # Yellow
        curses.init_pair(3, 4, -1)  # Blue

        self.state = True
        self.pause = False

        self.TICKRATE = 50

        self.KEYS = {"quit": (113, 27), # q and ESC
                     "pause": 112} # p

        self.ball = Ball.spawn(self.stdscr)

        self.player1 = Player(self.stdscr,
                              keys={"up": 119, "down": 115},
                              pos=Vector(3, curses.LINES//2 - self.ball.size.y * 3),
                              size=Vector(self.ball.size.x, self.ball.size.y * 3),
                              ch="%", color=2)

        self.player2 = Player(self.stdscr,
                              keys={"up": curses.KEY_UP, "down": curses.KEY_DOWN},
                              pos=Vector(curses.COLS - 3 - self.ball.size.x - 3,
                                         curses.LINES//2 - self.ball.size.y * 3),
                              size=Vector(self.ball.size.x, self.ball.size.y * 3),
                              ch="%", color=2)

    def printScore(self) -> None:
        score_str = f"{self.player1.score} | {self.player2.score}"
        utils.addstr(self.stdscr, self.rows//2 -
                     len(score_str), 0, score_str, 1)
        for i in range(0, self.rows):
            utils.addstr(self.stdscr, i, 1, "-")

    def input(self) -> None:
        key = self.stdscr.getch()
        if key in self.KEYS["quit"]:
            self.state = False
        elif key == self.KEYS["pause"]:
            self.pause = not self.pause

        self.player1.input(key)
        self.player2.input(key)

    def update(self) -> None:
        if not self.pause:
            self.ball.update()

            # Colisão bola e jogador 1
            if isCollidingX(self.ball, self.player1):
                self.ball.vel.x *= -1
                self.ball.collision = True

            # Colisão bola e jogador 2
            if (self.ball.x > self.player2.x - self.player2.sx and  # Direira da bola > esquerda do p2
                    self.ball.y + self.ball.sx > self.player2.y and  # Baixo da bola > cima do p2
                    self.ball.y < self.player2.y + self.player2.sy):  # Cima da bola < baixo do p2
                self.ball.vx = -self.ball.vx
                self.ball.collison = True

            # Cima da bola > parte de cima game
            if self.ball.y - self.ball.sy > 0:
                self.ball.vy = -self.ball.vy

            # Baixo da bola < parte de baixo game
            if self.ball.y + self.ball.sy < curses.LINES:
                self.ball.vy = -self.ball.vy

            # Direira da bola > parte da direita game
            if self.ball.x + self.ball.sx > curses.COLS - 2:
                self.player1.score += 1
                self.ball.reset()

            # Esquerda da bola < parte da esquerda game
            if self.ball.x - self.ball.sx < 2:
                self.player2.score += 1
                self.ball.reset()

    def render(self) -> None:
        self.stdscr.erase()

        # Score
        self.printScore()

        self.ball.render()
        self.player1.render()
        self.player2.render()

        self.stdscr.refresh()

    def loop(self) -> None:
        while self.state:
            self.input()

            self.update()

            self.render()

            curses.flushinp()  # Faz com que os inputs não se "arrastem"
            curses.napms(self.TICKRATE)


def main(stdscr) -> None:
    game = Game(stdscr)
    game.loop()


if __name__ == "__main__":
    curses.wrapper(main)
