import turtle

sc = turtle.Screen()

sc.title('Game 1')
sc.bgcolor('black')
sc.setup(width=800, height=600)
sc.tracer()

player = turtle.Turtle()

player.shape('circle')
player.color('white')
player.goto(0, 0)


def player_up():
    y = player.ycor()
    y += 20
    player.sety(y)

def player_down():
    y = player.ycor()
    y -= 20
    player.sety(y)    

def player_right():
    x = player.xcor()
    x += 20
    player.setx(x)

def player_left():
    x = player.xcor()
    x -= 20
    player.setx(x)    

sc.listen() 

sc.onkeypress(player_up, 'Up') 
sc.onkeypress(player_down, 'Down')
sc.onkeypress(player_right, 'Right')
sc.onkeypress(player_left, 'Left')

while True:
    sc.update()