import curses

class Game:
    def __init__(self):
        # Inicia a janela
        self.stdscr = curses.initscr()
        self.stdscr.nodelay(True)
        curses.cbreak()
        curses.noecho()
        curses.curs_set(0)
        
        # Colunas e filas todais
        self.cols, self.rows = self.stdscr.getmaxyx()
        self.state = True
        
        # Tamanho da bola
        self.sx_bola = 3
        self.sy_bola = 2
        
        # Coordenada da bola
        self.x_bola = self.rows//2
        self.y_bola = (self.cols//2)-3
        
        # Input
        self.key = ""

        

    def drawBox(self, x=0, y=0, sx=1, sy=1, ch="*"):
        """ Draw a full box
        Arguments:
            scr     - screen (window) to draw
            x, y    - start position (int)
            sx, sy  - length and height of the box (int)
            ch      - character to draw the box (str)
        """
        for j in range(y, sy+y):
            for i in range(x, sx+x, 2):
                self.stdscr.addstr(j, i, ch)

    def onRenderFrame(self):
        # stdscr.clear()
        self.drawBox(self.x_bola, self.y_bola, self.sx_bola, self.sy_bola)
        self.stdscr.addstr(5, 9, f"Key: {self.key}")
        self.stdscr.refresh()
   
    def onUpdateFrame(self):
        # self.x_bola += 1
        self.key = self.stdscr.getch()
        try:
            self.key=chr(self.key)
        except:
            pass
        if self.key == "q":
            self.state = False
    
    def main(self, stdscr):
        while self.state:
            self.onRenderFrame()
            self.onUpdateFrame()

if __name__ == "__main__":
    game = Game()
    curses.wrapper(game.main)

    
