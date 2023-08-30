import turtle as t


colors = ["red", "yellow", "blue", "green"]
t.pencolor("red")
for i in range(100):
    t.pencolor(colors[i % 4])
    t.forward(i)
    t.left(91)
    
