import curses

from Vector import Vector


def isCollidingEntityX(pos_a: Entity, pos_b: Entity) -> int:
    if (    ent_a.pos.x <= ent_b.pos.x + ent_b.size.x and # Esquerda < direita
            ent_a.pos.y + ent_a.size.y >= ent_b.pos.y and # Baixo > cima
            ent_a.pos.y <= ent_b.pos.y + ent_b.size.y): # Cima < baixo
        return True
    elif (  ent_a.pos.x >= ent_b.pos.x - ent_b.size.x and # Direita > esquerda
            ent_a.pos.y + ent_a.size.y >= ent_b.pos.y and # Baixo > cima
            ent_a.pos.y <= ent_b.pos.y + ent_b.size.y): # Cima < baixo
        return True
    return False

def isCollidingBoardX(ent: Entidy, board_left: int, board_right: int) -> bool:
    if ent.pos.x <= board_right: # Esquerda < direita
        return True
    elif ent.pos.x + ent.size.x >= board_left: # Direita > esquerda
        return True
    return False

def isCollidingBoardY(ent: Entidy, board_up: int, board_down: int) -> bool:
    if ent.pos.y <= board_up:
        return True
    elif ent.pos.y + ent.pos.y >= board_down:
        return True
    return False
