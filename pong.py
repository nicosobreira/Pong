from curses import wrapper

""" Grid System
Toda string tem que ser exibida com o eixo x que parece ser dobrada. Isso é por causa do aspect ratio (ex.: 1:2) por causa disso é necessário aumentar o eixo x, o eixo y se mantém intacto.
Um exemplo de como o Grid System funciona:
    ***       * * *
    ***  -->  * * *
    ***       * * *
"""


def main(stdscr):

    def drawBox(scr, x=0, y=0, dx=1, dy=1, ch="*"):
        """ Draw a full box
        Arguments:
            scr     - screen (window) to draw
            x, y    - start position (int)
            dx, dy  - length and height of the box (int)
            ch      - character to draw the box (str)
        """
        for j in range(y, dy+y):
            # O "dx + y + 3" é por causa do Grid System, as medidas são maiores para x do que para y
            for i in range(x, dx+(dx-1)+x, 2):
                scr.addstr(j, i, ch)

    def onUpdateFrame(*args):
        stdscr.getkey()

    def onRenderFrame(*args):
        cols, rows = stdscr.getmaxyx()
        stdscr.clear()
        drawBox(stdscr, 3, (cols//2)-6, 3, 6)
        drawBox(stdscr, rows-9, (cols//2)-5, 3, 6)
        drawBox(stdscr, rows//2, (cols//2)-3, 2, 2)
        stdscr.refresh()
    onRenderFrame()
    onUpdateFrame()


if __name__ == "__main__":
    game = True
    wrapper(main)
    while (game):
        main()
