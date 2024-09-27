from curses import wrapper

""" Grid System
Toda string tem que ser exibida com o eixo x que parece ser dobrada. Isso é por causa do aspect ratio (ex.: 1:2) por causa disso é necessário aumentar o eixo x, o eixo y se mantém intacto.
Um exemplo de como o Grid System funciona:
    ***       * * *
    ***  -->  * * *
    ***       * * *
"""

def drawBoxPoints(scr, x=0, y=0, dx=1, dy=1, ch="*"):
    scr.addstr(y, x, ch)
    scr.addstr(y, x + dx * 2, ch)
    scr.addstr(y + dy, x, ch)
    scr.addstr(y + dy, x + dx * 2, ch)


def drawLine(scr, p1=[0, 0], p2=[1, 0], ch="*"):
    x1 = p1[0] + 1
    y1 = p1[1]
    x2 = p2[0] + 1
    y2 = p2[1]
    for j in range(y1, y2+y1):
        for i in range(x1, x2+x1+2):
            scr.addstr(j, i, ch)

def drawBox_2(scr, x=0, y=0, dx=1, dy=1, ch="*"):
    x += 1
    for j in range(y, dy+1):
        for i in range(x, dx+2, 2):
            if j == y:
                scr.addstr(j, i, ch)

def drawBoxFull(scr, x=0, y=0, dx=1, dy=1, ch="*"):
    """ Draw a full box
    Arguments:
        x, y    - start position (int)
        dx, dy  - lenght and height of the box (int)
        ch      - character to draw the box (str)
    """
    for j in range(y, dy+y):
        # O "dx + y + 3" é por causa do Grid System, as medidas são maiores para x do que para y
        for i in range(x, dx+(dx-1)+x, 2):
            scr.addstr(j, i, ch)

def main(stdscr):
    stdscr.clear()
    # drawBox_1(stdscr, 3, 5, 2, 2)
    # drawBox_2(stdscr, dx=2, dy=2)
    drawBoxFull(stdscr, 3, 3, dx=3, dy=6)
    # drawLine(stdscr, p1=[1, 1])
    stdscr.refresh()
    stdscr.getkey()


if __name__ == "__main__":
    wrapper(main)
