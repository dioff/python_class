import turtle as t 

# for i in range(4):
#     t.forward(100)
#     t.left(90)
# t.done()

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        t.color(c)
        t.forward(steps)
        t.right(30)
# for i in range(3):
#     t.forward(100)
#     t.left(120)
# t.done()