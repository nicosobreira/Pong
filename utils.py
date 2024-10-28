from curses import color_pair

def addstr(scr, x: int, y: int, ch: str, color=0):
    scr.addstr(y, x, ch, color_pair(color))

def drawRect(scr, x: int, y: int, sx: int, sy: int, ch: str, color=0):
    """ Draw a full rectangle
        * A coordenada em x tem que ser: x + (x-1)
    """
    x = int(x)
    y = int(y)
    for j in range(y, sy + y):
        for i in range(x, sx + x, 2):
            addstr(scr, i, j, ch, color)
