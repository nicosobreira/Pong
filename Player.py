import curses

from collision import *

from Vector import Vector
from Entity import Entity
from Window import Window


class Player(Entity):
    def __init__(
        self,
        scr,
        KEYS: dict[str, int],
        pos: Vector,
        size: Vector,
        vel: Vector,
        score: int,
        ch="*",
        color=0
    ):
        super().__init__(scr, pos, size, vel, ch, color)
        self.KEYS = KEYS
        self.score = score

    @classmethod
    def new(
        cls,
        scr,
        KEYS: dict[str, int], 
        x: int,
        offset_x: int,
        size_mult_y: int,
        ball: Entity,
        board: Window,
        ch: str,
        color: int
    ):
        size = Vector(ball.size.x, ball.size.y * size_mult_y)
        pos = Vector(x + offset_x, board.middle_y - size.y // 2)
        score = 0
        vel = Vector(0, 2)

        return cls(scr, KEYS, pos, size, vel, score, ch, color)

    def input(self, key: int, board: Window):
        if (    key == self.KEYS["up"] and
                not self.pos.y - self.vel.y < board.up + 1):
            self.pos.y -= self.vel.y
        if (    key == self.KEYS["down"] and
                not self.pos.y + self.vel.y + self.size.y > board.down):
            self.pos.y += self.vel.y

    def render(self):
        super().render()
