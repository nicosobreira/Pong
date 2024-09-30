import curses


# TODO colocar um placar


def drawBox(stdscr, x=0, y=0, sx=1, sy=1, color_num=0, ch="*"):
    """ Draw a full box
    Arguments:
        scr     - screen (window) to draw
        x, y    - start position (int)
        sx, sy  - length and height of the box (int)
        color   - color pair to be used
        ch      - character to draw the box (str)
    """
    for j in range(y, sy+y):
        for i in range(x, sx+x, 2):
            stdscr.addstr(j, i, ch, curses.color_pair(color_num))

class Game:
    def __init__(self):
        # Inicia a janela
        self.stdscr = curses.initscr() # Inicia a janela
        self.stdscr.nodelay(True) # Se não tiver input o padrão é -1
        
        # Set color
        curses.start_color()
        curses.use_default_colors()

        # curses.cbreak() # 
        curses.noecho() # Não exibe os inputs
        curses.curs_set(0) # Não mostra o cursor
       
        # Color pairs
        curses.init_pair(1, 2, -1) # Green 
        curses.init_pair(2, 3, -1) # Yellow
        curses.init_pair(3, 4, -1) # Blue


        self.state = True
        
        self.TICKRATE = 50
        self.cols, self.rows = self.stdscr.getmaxyx()
        
        # Color pairs
        self.color_ball = 3
        self.color_player = 2
        self.color_score = 1
        
        # Caracter da bola
        self.char_bola = "o"

        # Tamanho da bola
        self.sx_bola = 3
        self.sy_bola = 2
        
        # Velocidade da bola
        self.vx_bola = 1
        self.vy_bola = 1
        
        # Coordenada da bola
        self.x_bola = self.rows//2
        self.y_bola = (self.cols//2) - self.sy_bola


        # Tamanho dos players
        self.sx_player = self.sx_bola
        self.sy_player = self.sy_bola * 3
        
        # Velocidade dos players
        self.v_player = 2
        
        # Coordenada dos players
        self.x_player1 = 3
        self.y_player1 = (self.cols//2) - self.sy_player
        self.x_player2 = self.rows - self.sx_player - 3
        self.y_player2 = (self.cols//2) - self.sy_player 
        
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

    def Update(self):
        self.x_bola += self.vx_bola
        self.y_bola += self.vy_bola
        
        # Colisão bola e jogador 1
        if (    self.x_bola < self.x_player1 + self.sx_player and # Esquerda da bola < direira do p1
                self.y_bola + self.sy_bola > self.y_player1 and # Baixo da bola > cima do p1
                self.y_bola < self.y_player1 + self.sy_player): # Cima da bola < direita do p1
            self.vx_bola = -self.vx_bola
        
        # Colisão bola e jogador 2
        if (    self.x_bola > self.x_player2 - self.sx_player and # Direira da bola > esquerda do p2
                self.y_bola + self.sy_bola > self.y_player2 and # Baixo da bola > cima do p2
                self.y_bola < self.y_player2 + self.sy_player): # Cima da bola < baixo do p2
            self.vx_bola = -self.vx_bola
        
        
        # Colisão bola lados e direito e esquerdo
        if (    self.x_bola + self.sx_bola > self.rows or
                self.x_bola - self.sx_bola < 0):
            self.score1 += 1
            self.vx_bola = -self.vx_bola
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
    
    def Render(self):
        self.stdscr.erase()
        
        # Render bola
        drawBox(self.stdscr, self.x_bola, self.y_bola, self.sx_bola, self.sy_bola, self.color_ball, self.char_bola)
        
        # Render player 1
        drawBox(self.stdscr, self.x_player1, self.y_player1, self.sx_player, self.sy_player, self.color_player)
        
        # Render player 2
        drawBox(self.stdscr, self.x_player2, self.y_player2, self.sx_player, self.sy_player, self.color_player)
        
        self.stdscr.refresh()
   
    def main(self, stdscr):
        while self.state:
            self.Update()
            self.Render()
            
            curses.flushinp() # Faz com que os inputs não se "arrastem"
            curses.napms(self.TICKRATE)

if __name__ == "__main__":
    game = Game()
    curses.wrapper(game.main)
