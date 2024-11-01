import random

from Vector import Vector
from Entity import Entity
from Window import Window


class Ball(Entity):
    def __init__(
        self,
        scr,
        pos: Vector,
        size: Vector,
        vel: Vector,
        ch: str, color: int
    ):
        super().__init__(scr, pos, size, vel, ch, color)

    @staticmethod
    def randomVelocity(
        vx_possible: tuple = (-2, 2),
        vy_possible: tuple = (-1, 1)
    ) -> Vector:
        return Vector(
            random.choice(vx_possible),
            random.choice(vy_possible)
        )

    @classmethod
    def new(cls, scr, board: Window, ch: str = "o", color: int = 0):
        size = Vector(3, 2)
        pos = Vector(board.middle_x, board.middle_y)
        vel = cls.randomVelocity()

        return cls(scr, pos, size, vel, ch, color)

    def reset(self, board: Window):
        self.pos.x = board.middle_x
        self.pos.y = board.middle_y
        self.vel = self.randomVelocity()
 
    def update(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y

    def render(self):
        super().render()
