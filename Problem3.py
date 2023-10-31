# Francisco Sanchez
# 10/28/23

import turtle

# Ask the user for input
num_sides = int(input("Enter the number of sides for the polygon: "))
side_length = int(input("Enter the length of each side: "))
line_color = input("Enter the color of the line: ")
fill_color = input("Enter the fill color: ")

# Create a turtle object
polygon = turtle.Turtle()

# Set the line and fill colors
polygon.color(line_color)
polygon.fillcolor(fill_color)

# Start filling
polygon. begin_fill()

# Draw the polygon
for _ in range(num_sides):
    polygon.forward(side_length)
    polygon.right(360 / num_sides)
# End filling
polygon.end_fill()

# Close the window when clicked
turtle.exitonclick()