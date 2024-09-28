import curses
""" Grid System
Toda string tem que ser exibida com o eixo x que parece ser dobrada. Isso é por causa do aspect ratio (ex.: 1:2) por causa disso é necessário aumentar o eixo x, o eixo y se mantém intacto.
Um exemplo de como o Grid System funciona:
    ***       * * *
    ***  -->  * * *
    ***       * * *
É por causa disso que todos os valores de x tem que ser = 2x-1
"""

game = True
x_bola = 3
y_bola = 2
key = ""
# drawBox(stdscr, rows-9, (cols//2)-5, 3, 6)
# drawBox(stdscr, 3, (cols//2)-6, 3, 6)
def main(stdscr):
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.clearok(True)

    def drawBox(scr, x=0, y=0, sx=1, sy=1, ch="*"):
        """ Draw a full box
        Arguments:
            scr     - screen (window) to draw
            x, y    - start position (int)
            sx, sy  - length and height of the box (int)
            ch      - character to draw the box (str)
        """
        for j in range(y, sy+y):
            for i in range(x, sx+x, 2):
                scr.addstr(j, i, ch)

    def onRenderFrame(*args):
        cols, rows = stdscr.getmaxyx()
        
        # stdscr.clear()
        drawBox(stdscr, rows//2, (cols//2)-3, x_bola, y_bola)
        stdscr.addstr(5, 5, f"Key: {key}")
        stdscr.refresh()
    
    def onUpdateFrame(*args):
        global x_bola
        global key
        # x_bola += 1
        key = stdscr.getch()
        if key == ord("q"):
            global game
            game = False
    
    while game:
        onRenderFrame()
        onUpdateFrame()


if __name__ == "__main__":
    curses.wrapper(main)
