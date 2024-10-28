from Vector import Vector

import utils

class Entity:
    def __init__(self, scr, pos: Vector, size: Vector, vel: Vector, ch: str, color: int) -> None:
        self.pos = pos
        self.size = size
        self.vel = vel

        self.ch = ch
        self.color = color

    def render(self) -> None:
        utils.drawRect(self.scr,
                       self.pos.x, self.pos.y,
                       self.size.x, self.size.y,
                       self.ch, self.color)
