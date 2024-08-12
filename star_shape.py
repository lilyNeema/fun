import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle to draw the star
star_turtle = turtle.Turtle()
star_turtle.shape("turtle")
star_turtle.color("yellow")
star_turtle.speed(2)

# Function to draw a star
def draw_star(size):
    for _ in range(5):
        star_turtle.forward(size)
        star_turtle.right(144)  # Angle for star shape

# Draw a star
draw_star(100)

# Hide the turtle and display the window
star_turtle.hideturtle()
turtle.done()

