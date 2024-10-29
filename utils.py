from curses import color_pair

from Window import Window
from Player import Player


def addstr(scr, x: int, y: int, ch: str, color: int) -> None:
    scr.addstr(y, x, ch, color_pair(color))

def drawPanel(scr,
              panel: Window,
              player1: Player, player2: Player,
              ch: str = "-", color: int = 0) -> None:
    drawLineX(scr, panel.left, panel.right, panel.up, ch, color)
    
    score_text = f"{player1.score | player2.score}"
    addstr(scr, panel.middle_x - len(score_text), panel.middle_y, ch, color)

    drawLineX(scr, panel.left, panel.right, panel.down, ch, color)

def drawPauseMessage(scr, board: Window):
    message = "PAUSE"
    addstr(scr, board.middle_x - len(message), board.middle_y, message, 0)

def drawLineX(scr, x: int, sx: int, y: int, ch: str, color: int = 0) -> None:
    for i in range(x, sx + x, 2):
        addstr(scr, i, y, ch, color)    

def drawLineY(scr, x: int, y: int, sy: int, ch: str, color: int = 0) -> None:
    for j in range(y, sy + x):
        addstr(scr, x, j, ch, color)    

def drawRect(scr, x: int, y: int, sx: int, sy: int, ch: str, color: int = 0) -> None:
    """ Draw a full rectangle
        * A coordenada em x tem que ser: x + (x-1)
    """
    for j in range(y, sy + y):
        for i in range(x, sx + x, 2):
            addstr(scr, i, j, ch, color)
