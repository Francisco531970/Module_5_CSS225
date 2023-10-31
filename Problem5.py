# Francisco Sanchez
# 10/28/23

import turtle

def draw_tree(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_tree(branch_length - 15, t)
        t.left(40)
        draw_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    tree_turtle = turtle.Turtle()
    tree_turtle.color("Green")
    tree_turtle.width(2)
    tree_turtle.left(90)
    tree_turtle.up()
    tree_turtle.goto(0, -200)
    tree_turtle.down()

    draw_tree(100, tree_turtle)

    screen.exitonclick()

if __name__ == "__main__":
    main()