import utils
from collision import *

from Vector import Vector
from Entity import Entity
from Window import Window


class Player(Entity):
    def __init__(self,
                 scr: int,
                 KEYS: dict,
                 pos: Vector,
                 size: Vector,
                 vel: Vector = Vector(5, 0),
                 ch="*", color=0) -> None:
        super().__init__(scr, pos, size, vel, ch, color)
        
        self.KEYS = KEYS

        self.score = 0

    def input(self, board: Window) -> None:
        key = self.scr.getch()
        if ( key == self.KEYS["up"] and
             isCollidingEntityBoardUp(self, board)):
            self.pos.y -= self.vel.y
        key = self.scr.getch()
        if ( key == self.KEYS["down"] and
             isCollidingEntityBoardDown(self, board)):
            self.pos.y += self.vel.y

    def render(self):
        super().render()
