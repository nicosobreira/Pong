import utils
from collision import *

from Vector import Vector
from Entity import Entity
from Window import Window


class Player(Entity):
    def __init__(self,
                 scr,
                 KEYS: dict,
                 pos: Vector,
                 size: Vector,
                 vel: Vector,
                 score: int,
                 ch="*", color=0) -> None:
        super().__init__(scr, pos, size, vel, ch, color)
        self.KEYS = KEYS
        self.score = score

    @classmethod
    def new(cls,
            scr,
            KEYS: dict, 
            x: int,
            offset_x: int,
            size_mult_y: int,
            ball: Entity,
            board: Window,
            ch: str = "%", color: int = 2):
        size = Vector(ball.size.x, ball.size.y * size_mult_y)
        pos = Vector(x + offset_x, board.middle_y - size.y // 2)
        score = 0
        vel = Vector(5, 0)

        return cls(scr, KEYS, pos, size, vel, score, ch, color)

    def input(self, key, board: Window) -> None:
        if ( key == self.KEYS["up"] and
             isCollidingEntityBoardUp(self, board)):
            self.pos.y -= self.vel.y
        if ( key == self.KEYS["down"] and
             isCollidingEntityBoardDown(self, board)):
            self.pos.y += self.vel.y

    def render(self):
        super().render()
