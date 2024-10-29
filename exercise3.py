import turtle


def get_depth():
    while True:
        depth = input('Enter the depth of the tree: ')
        if depth.isdigit():
            depth = int(depth)
            if depth > 0:
                return depth
            else:
                print('Please enter a positive number.')
        else:
            print('Please enter a number.')


def pifagor_tree(t, depth, size, left_tilt=5, right_tilt=2):
    if depth == 0:
        return
    t.forward(size)
    t.left(35 + left_tilt)
    pifagor_tree(t, depth - 1, size / 1.4, left_tilt + 5, right_tilt)
    t.right(70 + left_tilt + right_tilt)
    pifagor_tree(t, depth - 1, size / 1.7, left_tilt, right_tilt + 2)
    t.left(35 + right_tilt)
    t.backward(size)


def draw_tree(depth, size=800):
    window = turtle.Screen()
    window.bgcolor('white')

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -size / 3)
    t.setheading(90)
    t.pendown()

    pifagor_tree(t, depth, 200)
    window.mainloop()


draw_tree(get_depth())
