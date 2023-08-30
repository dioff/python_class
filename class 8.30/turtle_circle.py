import turtle as t 
import random
t.speed(0)
t.pencolor("red")

for i in range(10000000):
    t.right(random.randint(100, 1000))
    t.circle(random.randint(1, 100))
    
t.done()