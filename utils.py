import curses

from Window import Window
from Player import Player


def addstr(scr, x: int, y: int, ch: str, color: int) -> None:
    scr.addstr(y, x, ch, curses.color_pair(color))

def drawPanel(
    scr,
    panel: Window,
    player1: Player, player2: Player,
    chs: dict[str, str] = {"hor": "-", "ver": "|"},
    color: int = 0
) -> None:
    drawLineX(scr, panel.left, panel.up, panel.right, chs["hor"], color)
    drawLineX(scr, panel.left, panel.down, panel.right, chs["hor"], color)
    drawLineY(scr, panel.left, panel.up + 1, panel.down - 1, chs["ver"], color)
    drawLineY(scr, panel.right, panel.up + 1, panel.down - 1, chs["ver"], color)
    
    score_text = f"{player1.score} | {player2.score}"
    addstr(scr, panel.middle_x - len(score_text) // 2, panel.middle_y, score_text, 0)

def drawLineX(scr, x: int, y: int, sx: int, ch: str, color: int = 0) -> None:
    for i in range(x, sx, 2):
        addstr(scr, i, y, ch, color)    

def drawLineY(scr, x: int, y: int, sy: int, ch: str, color: int = 0) -> None:
    for j in range(y, sy + y):
        addstr(scr, x, j, ch, color)    

def drawRect(scr, x: int, y: int, sx: int, sy: int, ch: str, color: int = 0) -> None:
    """ Draw a full rectangle
        * A coordenada em x tem que ser: x + (x-1)
    """
    for j in range(y, sy + y):
        for i in range(x, sx + x, 2):
            addstr(scr, i, j, ch, color)
