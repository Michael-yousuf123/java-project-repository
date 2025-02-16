class Points:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = x
    def reset(self):
        self.x = 0
        self.y = 0
    def move(self, newx, newy):
        self.x = newx
        self.y = newy
    def moveX(self, newx):
        self.x = newx
    def moveY(self, newy):
        self.y = newy
    def showPoint(self):
        return f"({self.x},{self.y})"
if __name__ == "__main__":
    p1 = Points()
    p2 = Points(2, 4)
    p2.move(6, 9)
    print(p1.x, p1.y)
    print(p2.x, p2.y)
