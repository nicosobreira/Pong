import curses

from Vector import Vector
from Entity import Entity

import utils


class Ball(Entity):
    def __init__(self, scr,
                 pos: Vector,
                 size: Vector,
                 vel: Vector,
                 collision: bool,
                 ch: str, color: int) -> None:
        super().__init__(scr, pos, size, vel, ch, color)
        
        self.collision = collision

    @classmethod
    def spawn(cls, scr, ch: str = "o", color: int = 0) -> None:
        pos = Vector(curses.COLS, curses.LINES)
        size = Vector(3, 2)
        vel = Vector(1, 2)
        collision = False
        return cls(scr, pos, size, vel, collision, ch, color)

    def reset(self) -> None:
        self.pos.x = curses.COLS // 2 - self.size.x
        self.pos.y = curses.LINES // 2
        self.vel.x = -self.vel.x
 
    def update(self) -> None:
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y

    def render(self) -> None:
        super().render()
