def hexagon(t,x,y,w,color,sidelen):
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
    
    for i in  range (6):
        hexy.forward(sidelen)
        hexy.left(300)
    
wn= turtle.Screen
hexy= turtle.Turtle()

hexagon(hexy,0,0,1,"green",50)

polly=turtle.Turtle()
n= int(input("How many sides do you want in your polygon?"))
l= int(input("What is the length of the sides?"))

for i in range (n):
    polly.forward(l)
    polly.right(360/n)
