import curses

from Vector import Vector
from Entity import Entity

import utils


class Player(Entity):
    def __init__(self, scr,
                 keys: dict,
                 pos: Vector,
                 size: Vector,
                 vel: Vector = Vector(5, 0),
                 ch="*", color=0) -> None:
        super().__init__(scr, pos, size, vel, ch, color)
        
        # Dicionário das teclas
        self.keys = keys

        self.score = 0

    def input(self, key: int) -> None:
        if (    key == self.keys["up"] and
                self.pos.y - self.vel.y > 2):
            self.pos.y -= self.vel.y * 0.001

        if (    key == self.keys["down"] and
                self.pos.y + self.size.y + self.vel.y < curses.COLS):
            self.pos.y += self.vel.y * 0.001

    def render(self):
        super().render()
