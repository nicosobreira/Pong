import curses
import utils

from Ball import Ball
from Player import Player


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
       
        self.KEYS = {"quit": 113} # q

        self.ball = Ball(self.stdscr,
                    self.rows//2 - 3,
                    self.cols//2,
                    3,
                    2,
                    "o",
                    3)

        self.player1 = Player(self.stdscr,
                         {"up": 119, "down": 115},
                         3,
                         ((self.cols//2) - self.ball.sy * 3),
                         self.ball.sx,
                         (self.ball.sy * 3),
                         "%",
                         2)
        
        self.player2 = Player(self.stdscr,
                         {"up": curses.KEY_UP, "down": curses.KEY_DOWN},
                         (self.rows - 3 - self.ball.sx - 3),
                         (self.cols//2) - self.ball.sy * 3,
                         self.ball.sx,
                         (self.ball.sy * 3),
                         "%",
                         2)
        
        # Input
        self.key = ""


    def printScore(self):
        score_str = f"{self.player1.score} | {self.player2.score}"
        utils.addstr(self.stdscr, self.rows//2 - len(score_str), 0, score_str, 1)
        for i in range(0, self.rows):
            utils.addstr(self.stdscr, i, 1, "-")


    def Update(self):
        self.ball.x += self.ball.vx
        self.ball.y += self.ball.vy
        
        # Colisão bola e jogador 1
        if (    self.ball.x < self.player1.x + self.player1.sx and # Esquerda da bola < direira do p1
                self.ball.y + self.ball.sy > self.player1.y and # Baixo da bola > cima do p1
                self.ball.y < self.player1.y + self.player1.sy): # Cima da bola < direita do p1
            self.ball.vx = -self.ball.vx
            self.ball.collision = True
        
        # Colisão bola e jogador 2
        if (    self.ball.x > self.player2.x - self.player2.sx and # Direira da bola > esquerda do p2
                self.ball.y + self.ball.sx > self.player2.y and # Baixo da bola > cima do p2
                self.ball.y < self.player2.y + self.player2.sy): # Cima da bola < baixo do p2
            self.ball.vx = -self.ball.vx
            self.ball.collison = True
        
        # Cima da bola > parte de cima game
        if self.ball.y - self.ball.sy > 0: 
            self.ball.vy = -self.ball.vy
       
        # Baixo da bola < parte de baixo game
        if self.ball.y + self.ball.sy < self.cols: 
            self.ball.vy = -self.ball.vy
        
        # Direira da bola > parte da direita game
        if self.ball.x + self.ball.sx > self.rows - 2: 
            self.player1.score += 1
            self.ball.reset(self.rows, self.cols)
        
        # Esquerda da bola < parte da esquerda game
        if self.ball.x - self.ball.sx < 2: 
            self.player2.score += 1
            self.ball.reset(self.rows, self.cols)
        
        key = self.stdscr.getch()
        
        self.player1.input(key, self.cols)
        self.player2.input(key, self.cols)
        
        if key == self.KEYS["quit"]:
            self.state = False


    def Render(self):
        self.stdscr.erase()
        
        # Score
        self.printScore()

        self.ball.render()
        self.player1.render() 
        self.player2.render()
        
        self.stdscr.refresh()
 

    def Loop(self, stdscr):
        while self.state:
            self.Update()
            self.Render()
            
            curses.flushinp() # Faz com que os inputs não se "arrastem"
            curses.napms(self.TICKRATE)


if __name__ == "__main__":
    game = Game()
    curses.wrapper(game.Loop)
