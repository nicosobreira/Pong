import curses

class Game:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.state = True
        self.x_bola = 3
        self.y_bola = 2

    def drawBox(self, scr, x=0, y=0, sx=1, sy=1, ch="*"):
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

    def onRenderFrame(self):
        cols, rows = self.stdscr.getmaxyx()
        
        # stdscr.clear()
        drawBox(self.stdscr, rows//2, (cols//2)-3, self.x_bola, self.y_bola)
        stdscr.addstr(5, 5, f"Key: {key}")
        stdscr.refresh()
    
    def onUpdateFrame(self):
        self.x_bola
        # x_bola += 1
        key = self.stdscr.getch()
        try:
            key=chr(key)
        except:
            pass
        if key == "q":
            self.game = False

    def main(self, stdscr):
        while self.state:
            onRenderFrame()
            onUpdateFrame()

if __name__ == "__main__":
    game = curses.wrapper(Game)
    game.main()
