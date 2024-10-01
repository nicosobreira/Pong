import utils


class Player:
    def __init__(self, scr, KEYS: dict, x: int, y: int, sx: int, sy: int, ch="*", color=0) -> None:
        self.scr = scr
        
        # Dicionário das teclas
        self.KEYS = KEYS
        
        # Posição
        self.x = x
        self.y = y

        # Tamanho
        self.sx = sx
        self.sy = sy

        # Velocidade
        self.v = 2
       
        # Render
        self.ch = ch
        self.color = color

        self.score = 0


    def render(self):
        utils.drawRect(self.scr, self.x, self.y, self.sx, self.sy, self.ch, self.color)


    def input(self, key, cols):
        if (    key == self.KEYS["up"] and
                self.y - self.v > 2):
            self.y -= self.v

        if (    key == self.KEYS["down"] and
                self.y + self.sy + self.v < cols):
            self.y += self.v
