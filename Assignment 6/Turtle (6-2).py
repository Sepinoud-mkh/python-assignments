import turtle

pen=turtle.Pen()
side=3

while side>=3:
    degree=((side-2)*180)/side
    pen.left(180-degree/2)
    
    for i in range(side):
        pen.forward(70*(1+side/10))
        pen.left(180-degree)
    
    pen.right(180-degree/2)
    pen.penup()
    pen.forward(12*(1+side/10))
    pen.pendown()
    
    side=side+1

turtle.done()
