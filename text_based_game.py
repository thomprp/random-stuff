import sys, random
class display():
    def __init__(self,player):
        # Map
        self.lineOneData = [(0,0), (1,0), (2,0), (3,0), (4,0)]
        self.lineTwoData = [(0,1), (1,1), (2,1), (3,1), (4,1)]
        self.lineThreeData = [(0,2), (1,2), (2,2), (3,2), (4,2)]
        self.lineFourData = [(0,3), (1,3), (2,3), (3,3), (4,3)]
        self.lineFiveData = [(0,4), (1,4), (2,4), (3,4), (4,4)]

        self.lineOneDisplay = ["P", "o", "o", "o", "o"]
        self.lineTwoDisplay = ["o", "o", "o", "o", "o"]
        self.lineThreeDisplay = ["o", "o", "F", "o", "o"]
        self.lineFourDisplay = ["o", "o", "o", "o", "o"]
        self.lineFiveDisplay = ["o", "o", "o", "o", "o"]
    def draw(self):
        print(f"{self.lineOneDisplay}\n{self.lineTwoDisplay}\n{self.lineThreeDisplay}\n{self.lineFourDisplay}\n{self.lineFiveDisplay}\n")
    def reset(self):
        self.lineOneDisplay = ["o", "o", "o", "o", "o"]
        self.lineTwoDisplay = ["o", "o", "o", "o", "o"]
        self.lineThreeDisplay = ["o", "o", "o", "o", "o"]
        self.lineFourDisplay = ["o", "o", "o", "o", "o"]
        self.lineFiveDisplay = ["o", "o", "o", "o", "o"]
    def update(self,player, fruit):
        if player.y == 0:
            if player.x == 0:
                self.lineOneDisplay[0] = "P"
            if player.x == 1:
                self.lineOneDisplay[1] = "P"
            if player.x == 2:
                self.lineOneDisplay[2] = "P"
            if player.x == 3:
                self.lineOneDisplay[3] = "P"
            if player.x == 4:
                self.lineOneDisplay[4] = "P"
        elif player.y == 1:
            if player.x == 0:
                self.lineTwoDisplay[0] = "P"
            if player.x == 1:
                self.lineTwoDisplay[1] = "P"
            if player.x == 2:
                self.lineTwoDisplay[2] = "P"
            if player.x == 3:
                self.lineTwoDisplay[3] = "P"
            if player.x == 4:
                self.lineTwoDisplay[4] = "P"
        elif player.y == 2:
            if player.x == 0:
                self.lineThreeDisplay[0] = "P"
            if player.x == 1:
                self.lineThreeDisplay[1] = "P"
            if player.x == 2:
                self.lineThreeDisplay[2] = "P"
            if player.x == 3:
                self.lineThreeDisplay[3] = "P"
            if player.x == 4:
                self.lineThreeDisplay[4] = "P"
        elif player.y == 3:
            if player.x == 0:
                self.lineFourDisplay[0] = "P"
            if player.x == 1:
                self.lineFourDisplay[1] = "P"
            if player.x == 2:
                self.lineFourDisplay[2] = "P"
            if player.x == 3:
                self.lineFourDisplay[3] = "P"
            if player.x == 4:
                self.lineFourDisplay[4] = "P"
        elif player.y == 4:
            if player.x == 0:
                self.lineFiveDisplay[0] = "P"
            if player.x == 1:
                self.lineFiveDisplay[1] = "P"
            if player.x == 2:
                self.lineFiveDisplay[2] = "P"
            if player.x == 3:
                self.lineFiveDisplay[3] = "P"
            if player.x == 4:
                self.lineFiveDisplay[4] = "P"
        if fruit.y == 0:
            if fruit.x == 0:
                self.lineOneDisplay[0] = "F"
            if fruit.x == 1:
                self.lineOneDisplay[1] = "F"
            if fruit.x == 2:
                self.lineOneDisplay[2] = "F"
            if fruit.x == 3:
                self.lineOneDisplay[3] = "F"
            if fruit.x == 4:
                self.lineOneDisplay[4] = "F"
        elif fruit.y == 1:
            if fruit.x == 0:
                self.lineTwoDisplay[0] = "F"
            if fruit.x == 1:
                self.lineTwoDisplay[1] = "F"
            if fruit.x == 2:
                self.lineTwoDisplay[2] = "F"
            if fruit.x == 3:
                self.lineTwoDisplay[3] = "F"
            if fruit.x == 4:
                self.lineTwoDisplay[4] = "F"
        elif fruit.y == 2:
            if fruit.x == 0:
                self.lineThreeDisplay[0] = "F"
            if fruit.x == 1:
                self.lineThreeDisplay[1] = "F"
            if fruit.x == 2:
                self.lineThreeDisplay[2] = "F"
            if fruit.x == 3:
                self.lineThreeDisplay[3] = "F"
            if fruit.x == 4:
                self.lineThreeDisplay[4] = "F"
        elif fruit.y == 3:
            if fruit.x == 0:
                self.lineFourDisplay[0] = "F"
            if fruit.x == 1:
                self.lineFourDisplay[1] = "F"
            if fruit.x == 2:
                self.lineFourDisplay[2] = "F"
            if fruit.x == 3:
                self.lineFourDisplay[3] = "F"
            if fruit.x == 4:
                self.lineFourDisplay[4] = "F"
        elif fruit.y == 4:
            if fruit.x == 0:
                self.lineFiveDisplay[0] = "F"
            if fruit.x == 1:
                self.lineFiveDisplay[1] = "F"
            if fruit.x == 2:
                self.lineFiveDisplay[2] = "F"
            if fruit.x == 3:
                self.lineFiveDisplay[3] = "F"
            if fruit.x == 4:
                self.lineFiveDisplay[4] = "F"
    def quit():
        sys.exit()

class player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1
    def move(self):
        self.user = str(input("W A S D\n"))
        self.user = self.user.upper()
        if self.user == "W":
            self.y -= 1
        elif self.user == "A":
            self.x -= 1
        elif self.user == "S":
            self.y += 1
        elif self.user == "D":
            self.x += 1
        else:
            print("Error. Input Malfunction.")
class fruit():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.collected = False
    def collected(self,player):
        if self.x == player.x and self.y == player.y:
            print("lol")
            self.collected = True
            return self.collected
        else:
            pass
    def spawn(self):
        if self.collected:
            self.x = random.randint(0,4)
            self.y = random.randint(0,4)
            self.collected = False
        else:
            pass

Fruit = fruit(2, 2)
Player = player(0, 0)
Display = display(Player)
run = True
while run:
    Display.draw()
    Player.move()
    Fruit.collected(Player)
    Fruit.spawn()
    # stuffff
    Display.reset()
    Display.update(Player, Fruit)