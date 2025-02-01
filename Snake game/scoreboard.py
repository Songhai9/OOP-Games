from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.write(f'Score : {self.score} | High Score : {self.high_score}', False, align='center')
        

    def update_score(self):
        self.clear()
        self.write(f'Score : {self.score} | High Score : {self.high_score}', False, align='center')
    
    def game_over(self):
        self.goto(x=0, y=0)
        self.write('GAME OVER')
    
    def reset(self):
        if self.score > self.high_score:
            with open('data.txt', 'w') as data:
                self.high_score = self.score
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_score()
        