import utils


class Ball:
    def __init__(self, scr, x: int, y: int, sx: int, sy: int, ch="o", color=0) -> None:
        self.scr = scr
        
        # Coordenadas
        self.x = x
        self.y = y
        
        # Tamanho
        self.sx = sx
        self.sy = sy
        
        # Velocidade
        self.vx = 1
        self.vy = 1
        
        # Render
        self.ch = ch
        self.color = color

        self.collision = False
    

    def reset(self, rows, cols):
        self.x = (rows // 2) - self.sx
        self.y = cols // 2
        self.vx = -self.vx
 
 
    def render(self):
        utils.drawRect(self.scr, self.x, self.y, self.sx, self.sy, self.ch, self.color)
