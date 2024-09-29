import curses
from time import sleep

TICKRATE = 50

def drawBox(stdscr, x=0, y=0, sx=1, sy=1, ch="*"):
    """ Draw a full box
    Arguments:
        scr     - screen (window) to draw
        x, y    - start position (int)
        sx, sy  - length and height of the box (int)
        ch      - character to draw the box (str)
    """
    for j in range(y, sy+y):
        for i in range(x, sx+x, 2):
            stdscr.addstr(j, i, ch)

class Player():
    def __init__(self, x, y, sx, sy):
        self.x_player = x
        self.y_player = y
        
        # Tamanho
        self.sx_player = sx
        self.sy_player = sy
        
        # Velocidade
        self.v_player = 1
    
    # def collision(self):

class Game:
    def __init__(self):
        # Inicia a janela
        self.stdscr = curses.initscr()
        self.stdscr.nodelay(True)
        curses.cbreak()
        curses.noecho()
        curses.curs_set(0)
        
        self.cols, self.rows = self.stdscr.getmaxyx()
        self.state = True
        
        # Tamanho da bola
        self.sx_bola = 3
        self.sy_bola = 2
        
        # Velocidade da bola
        self.vx_bola = 1
        self.vy_bola = 1
        
        # Coordenada da bola
        self.x_bola = self.rows//2
        self.y_bola = (self.cols//2)-3
        
        # Tamanho dos players
        self.sx_player = self.sx_bola
        self.sy_player = self.sy_bola * 3
        
        # Velocidade dos players
        self.v_player = 1
        
        # Coordenada dos players
        self.x_player1 = 0
        self.y_player1 = self.cols//2
        self.x_player2 = self.rows - self.sx_player
        self.y_player2 = self.cols//2
        
        # Pontos
        self.score1 = 0
        self.score2 = 0
        
        # Input
        self.key = ""

    def resetBall(self):
        self.x_bola = self.rows//2
        self.y_bola = (self.cols//2)-3

    def printScore(self):
        self.stdscr.addstr()

    def onUpdateFrame(self):
        self.x_bola += self.vx_bola
        self.y_bola += self.vy_bola
        
        if self.x_bola < self.x_player2 - self.sx_player:
            self.vx_bola = -self.vx_bola
        
        # Colisão da bola
        # Direita
        if self.x_bola + self.sx_bola < self.rows:
            self.score1 += 1
            self.resetBall()
        
        # Esquerda
        if self.x_bola - self.sx_bola > 0:
            self.score2 += 1
            self.resetBall()
        
        # Cima
        if self.y_bola - self.sy_bola > 0:
            self.vy_bola = -self.vy_bola
        
        # Baixo
        if self.y_bola + self.sy_bola < self.cols:
            self.vy_bola = -self.vy_bola
        
        # Input
        self.key = self.stdscr.getch()
        
        # Player 1
        if self.key == 119: # w
            self.y_player1 -= self.v_player
        if self.key == 115: # s
            self.y_player1 += self.v_player

        # Player 2
        if self.key == curses.KEY_UP:
            self.y_player2 -= self.v_player
        if self.key == curses.KEY_DOWN:
            self.y_player2 += self.v_player
        
        # Game
        if self.key == 113: # q
            self.state = False
    
    def onRenderFrame(self):
        self.stdscr.erase()
        drawBox(self.stdscr, self.x_bola, self.y_bola, self.sx_bola, self.sy_bola)
        drawBox(self.stdscr, self.x_player1, self.y_player1, self.sx_player, self.sy_player)
        drawBox(self.stdscr, self.x_player2, self.y_player2, self.sx_player, self.sy_player)
        # self.stdscr.addstr(5, 9, f"Key: {self.key}")
        # self.printScore()
        self.stdscr.refresh()
   
    def main(self, stdscr):
        while self.state:
            self.onUpdateFrame()
            self.onRenderFrame()
            
            # Faz com que os inputs não se "arrastem"
            curses.flushinp()
            curses.napms(TICKRATE)

if __name__ == "__main__":
    game = Game()
    curses.wrapper(game.main)

    
