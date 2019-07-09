from turtle import *
shape('turtle')
color('blue')
speed(0)

for i in range(56):
    left(30)
    forward(i+1)
    left(90)
    forward(i+1)
    left(90)
    forward(i+1)
    left(90)
    forward(i+1)
    left(75)

mainloop()