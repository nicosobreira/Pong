class Window:
    def __init__(self, left: int, right: int, up: int, down: int) -> None:
        self.left = left
        self.right = right
        self.up = up
        self.down = down

        self.middle_x = round(self.right / 2)
        self.middle_y = round(self.down / 2)