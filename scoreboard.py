from turtle import Turtle
ALINHAMENTO = 'center'
FONTE = ("Courier", 15, "normal")


class Placar(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_placar()

    def update_placar(self):
        self.write(f'Score: {self.score}', align=ALINHAMENTO , font=FONTE)


    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write(f'GAME OVER', align=ALINHAMENTO , font=("Courier", 20, "normal"))



    def aumentarplacar(self):
        self.score += 1
        self.clear()
        self.update_placar()