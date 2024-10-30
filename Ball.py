import curses

import utils

from Vector import Vector
from Entity import Entity
from Window import Window


class Ball(Entity):
    def __init__(self, scr,
                 pos: Vector,
                 size: Vector,
                 vel: Vector,
                 ch: str, color: int) -> None:
        super().__init__(scr, pos, size, vel, ch, color)

    @classmethod
    def new(cls, scr, board: Window, ch: str = "o", color: int = 0) -> None:
        pos = Vector(board.middle_x, board.middle_y)
        size = Vector(3, 2)
        vel = Vector(1, 2)

        return cls(scr, pos, size, vel, ch, color)

    def reset(self, board: Window) -> None:
        self.pos.x = board.middle_x - self.size.x // 2
        self.pos.y = board.middle_y - self.size.y // 2
        self.vel.x *= -1
 
    def update(self) -> None:
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y

    # def render(self) -> None:
    #     super().render()
