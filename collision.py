from Entity import Entity
from Window import Window


def isCollidingEntityLeftRight(ent_a: Entity, ent_b: Entity) -> bool:
    if (    ent_a.pos.x < ent_b.pos.x + ent_b.size.x and # Esquerda < direita
            ent_a.pos.y + ent_a.size.y > ent_b.pos.y and # Baixo > cima
            ent_a.pos.y < ent_b.pos.y + ent_b.size.y): # Cima < baixo
        return True
    return False


def isCollidingEntityRightLeft(ent_a: Entity, ent_b: Entity) -> bool:
    if (    ent_a.pos.x + ent_a.size.x > ent_b.pos.x and # Direita > esquerda
            ent_a.pos.y + ent_a.size.y > ent_b.pos.y and # Baixo > cima
            ent_a.pos.y < ent_b.pos.y + ent_b.size.y): # Cima < baixo
        return True
    return False


def isCollidingEntityBoardLeft(ent: Entity, board: Window) -> bool:
    if ent.pos.x < board.left:
        return True
    return False


def isCollidingEntityBoardRight(ent: Entity, board: Window) -> bool:
    if ent.pos.x + ent.size.x > board.right:
        return True
    return False


def isCollidingEntityBoardUp(ent: Entity, board: Window) -> bool:
    if ent.pos.y - ent.size.y < board.up:
        return True
    return False


def isCollidingEntityBoardDown(ent: Entity, board: Window) -> bool:
    if ent.pos.y + ent.vel.y + ent.size.y > board.down:
        return True
    return False
