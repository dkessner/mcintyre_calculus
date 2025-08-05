from turtle import Turtle, tracer, setup, Screen
import numpy as np


# Set the window dimensions.
WIDTH = 400
HEIGHT = 400
PAD = 5
x_max = int(WIDTH / 2)
x_min = -x_max
y_max = int(HEIGHT / 2)
y_min = -y_max

# Resize the window.
setup(WIDTH + PAD, HEIGHT + PAD)

# Create a plotting turtle and hide it while drawing.
plot_turtle = Turtle()
plot_turtle.hideturtle()


def draw_axis(x_start, y_start, x_end, y_end):
    """Draws an axis between two points."""    
    tracer(0)
    
    # Set the drawing color.
    plot_turtle.color("gray0")
    
    # Go to the start position.
    plot_turtle.penup()
    plot_turtle.goto(x_start, y_start)
    
    # Point towards the end position.
    heading = plot_turtle.towards(x_end, y_end)
    plot_turtle.seth(heading)
    
    # Draw the line.
    plot_turtle.pensize(1)
    plot_turtle.pendown()
    plot_turtle.goto(x_end, y_end)
    
    # Stamp the turtle's shape.
    plot_turtle.penup()
    plot_turtle.forward(3)
    plot_turtle.stamp()

    tracer(1)


def draw_axes():
    """Draws the x- and y-axes."""
    
    # x-axis
    draw_axis(x_min, 0, x_max - 11, 0)
    
    # y-axis
    draw_axis(0, y_min, 0, y_max - 3)


def plot(f, color="gray0"):
    """Plots a function in a given color."""
    tracer(0)
    
    plot_turtle.penup()
    
    # Go to the starting point.
    x_start = x_min
    y_start = f(x_min)
    plot_turtle.goto(x_start, y_start)
    
    # Plot the function.
    plot_turtle.pencolor(color)
    plot_turtle.pensize(2)
    plot_turtle.pendown()
    for x in range(x_min, x_max, 1):
        y = f(x)
        plot_turtle.goto(x, y)
    
    tracer(1)


def clear():
    """Clears the Turtle Graphics window."""
    tracer(0)
    
    plot_turtle.reset()
    plot_turtle.hideturtle()

    tracer(1)


def diff(f, x, dx=0.0001):
    """Estimates a function's derivative with a forward difference."""
    df = f(x + dx) - f(x)
    return df / dx


def draw_tangent(f, x, color="gray60", length=200, dx=0.0001):
    """Draws a tangent line."""
    tracer(0)
    plot_turtle.penup()
    
    # Go to the point of tangency.
    y = f(x)
    plot_turtle.goto(x, y)
    
    # Draw the point of tangency.
    plot_turtle.color(color)
    plot_turtle.pendown()
    plot_turtle.pensize(3)
    plot_turtle.dot()
    
    # Calculate a point along the tangent line.
    x1 = x + dx
    y1 = y + dx * diff(f, x, dx)
    
    # Point the turtle along the tangent line.
    angle = plot_turtle.towards(x1, y1)
    plot_turtle.seth(angle)
    
    # Draw the tangent line.
    plot_turtle.pensize(1)
    plot_turtle.forward(0.5 * length)
    plot_turtle.back(length)
    
    tracer(1)


def left_sum(f, x_start, x_end, dx=0.0001):
    """Estimates a function's integral with a left Riemann sum."""
    integral = 0
    x = x_start
    while x < x_end:
        integral += f(x) * dx
        x += dx
    return integral


def draw_rect(x, y, width, height, stroke, fill=None):
    """Draws a rectangle that can be filled with a given color."""
    plot_turtle.pencolor(stroke)
    plot_turtle.pensize(1)
    if fill != None:
        plot_turtle.fillcolor(fill)
        plot_turtle.begin_fill()
    plot_turtle.begin_poly()
    plot_turtle.goto(x, y)
    plot_turtle.goto(x, y + height)
    plot_turtle.goto(x + width, y + height)
    plot_turtle.goto(x + width, y)
    plot_turtle.goto(x, y)
    plot_turtle.end_poly()
    if fill != None:
        plot_turtle.end_fill()


def draw_riemann(f, x_start, x_end, dx, stroke, fill=None):
    """Fills the area beneath a curve with rectangles."""
    tracer(0)
    
    # Go to the starting point.
    plot_turtle.penup()
    plot_turtle.goto(x_start, 0)
    plot_turtle.pendown()

    # Draw the rectangles.
    x = x_start
    y = 0
    while x < x_end:
        width = dx
        height = f(x)
        draw_rect(x, y, width, height, stroke, fill)
        x += dx
    
    tracer(1)


def draw_vector(pos, vec, color="gray50"):
    """Draws a vector as an arrow."""
    plot_turtle.penup()
    plot_turtle.goto(pos)
    plot_turtle.pendown()
    plot_turtle.pensize(1)
    plot_turtle.color(color)
    angle = plot_turtle.towards(pos + vec)
    mag = abs(vec)
    plot_turtle.seth(angle)
    plot_turtle.forward(mag)
    plot_turtle.stamp()
    plot_turtle.penup()


def draw_grid(spacing=50, color="gray80"):
    """Draws horizontal and vertical lines."""
    tracer(0)

    # Go to the origin.
    plot_turtle.penup()
    plot_turtle.goto(0, 0)

    # Draw vertical lines.
    plot_turtle.pencolor(color)
    plot_turtle.pensize(1)
    for x in range(0, x_max, spacing):
        plot_turtle.penup()
        plot_turtle.goto(x, y_min)
        plot_turtle.pendown()
        plot_turtle.goto(x, y_max)
        plot_turtle.penup()
        plot_turtle.goto(-x, y_min)
        plot_turtle.pendown()
        plot_turtle.goto(-x, y_max)
    
    # # Go to the origin.
    plot_turtle.penup()
    plot_turtle.goto(0, 0)
    
    # Draw horizontal lines.
    for y in range(0, y_max, spacing):
        plot_turtle.penup()
        plot_turtle.goto(x_min, y)
        plot_turtle.pendown()
        plot_turtle.goto(x_max, y)
        plot_turtle.penup()
        plot_turtle.goto(x_min, -y)
        plot_turtle.pendown()
        plot_turtle.goto(x_max, -y)

    tracer(1)


def draw_xlabel(text, color="gray0", font=("Courier New", 20, "normal")):
    """Draws the label for the x-axis."""
    tracer(0)

    plot_turtle.penup()
    plot_turtle.color(color)
    plot_turtle.goto(x_max - 20, 10)
    plot_turtle.write(text, align="right", font=font)

    tracer(1)


def draw_ylabel(text, color="gray0", font=("Courier New", 20, "normal")):
    """Draws the label for the y-axis."""
    tracer(0)

    plot_turtle.penup()
    plot_turtle.color(color)
    plot_turtle.goto(10, y_max - 20)
    plot_turtle.write(text, align="left", font=font)

    tracer(1)


def draw_title(text, color="gray0", font=("Courier New", 20, "normal")):
    """Draws the title."""
    tracer(0)

    plot_turtle.penup()
    plot_turtle.color(color)
    plot_turtle.goto(x_min, y_max - 20)
    plot_turtle.write(text, align="left", font=font)

    tracer(1)


vector_field = []


def create_field(spacing=50, color="gray80"):
    """Create a list of Turtles to visualize a vector field."""
    tracer(0)

    for x in range(x_min, x_max + 1, spacing):
        for y in range(y_min, y_max + 1, spacing):
            t = Turtle()
            t.speed(0)
            t.hideturtle()
            t.color(color)
            t.penup()
            t.goto(x, y)
            vector_field.append(t)

    tracer(1)


def hide_field():
    """Hide the Turtle objects used to draw vector fields."""
    tracer(0)

    for t in vector_field:
        t.hideturtle()
    
    tracer(1)


def show_field():
    """Show the Turtle objects used to draw vector fields."""
    tracer(0)

    for t in vector_field:
        t.showturtle()
    
    tracer(1)


# Create the vector field and hide it.
create_field()
hide_field()


def draw_field(field, scale=0.007, min_scale=0.001):
    """Draw a vector field using arrows."""
    show_field()

    tracer(0)

    for t in vector_field:
        # Calculate the field.
        state = t.pos()
        change = field(state)
        # Find a point along the field.
        next_state = state + change
        angle = t.towards(next_state)
        t.seth(angle)
        # Set the turtle's size based on the
        # field's magnitude.
        size = abs(change) * scale + min_scale
        t.shapesize(size)
    
    tracer(1)


def integrate_field(field, initial_state, t_f, dt=0.0001):
    """Integrates a vector field and return a trajectory."""
    trajectory = [initial_state]
    num_steps = int(t_f / dt)
    num_vars = len(initial_state)
    
    for i in range(1, num_steps):
        state = trajectory[i - 1]
        change = field(state)
        next_state = []
        for j in range(num_vars):
            next_state.append(state[j] + dt * change[j])
        trajectory.append(next_state)
    
    return trajectory


def draw_trajectory(trajectory, color="gray0"):
    """Draws a trajectory through a vector field."""
    tracer(0)

    # Prepare to draw.
    initial_state = trajectory[0]
    plot_turtle.penup()
    plot_turtle.goto(initial_state)
    plot_turtle.pendown()
    plot_turtle.pensize(1)
    plot_turtle.color(color)

    # Integrate the vector field.
    for state in trajectory:
        plot_turtle.goto(state)
    
    tracer(1)


def translate2D(tx, ty):
    """Returns a 2D translation matrix."""
    T = np.array([[1, 0, tx],
                  [0, 1, ty],
                  [0, 0, 1]])
    return T


def rotate2D(angle):
    """Returns a 2D rotation matrix."""
    c = np.cos(angle)
    s = np.sin(angle)
    R = np.array([[c, -s, 0],
                  [s,  c, 0],
                  [0,  0, 1]])
    return R


def scale2D(sx, sy):
    """Returns a 2D scale matrix."""
    S = np.array([[sx,  0, 0],
                  [ 0, sy, 0],
                  [ 0,  0, 1]])
    return S


def translate3D(tx, ty, tz):
    """Returns a 3D translation matrix."""
    T = np.array([[1, 0, 0, tx],
                  [0, 1, 0, ty],
                  [0, 0, 1, tz],
                  [0, 0, 0,  1]])
    return T


def scale3D(sx, sy, sz):
    """Returns a 3D scale matrix."""
    S = np.array([[sx,   0,  0, 0],
                  [ 0,  sy,  0, 0],
                  [ 0,   0, sz, 0],
                  [ 0,   0,  0, 1]])
    return S


def rotate_x(angle):
    """Returns a 3D rotation matrix about the x-axis."""
    c = np.cos(angle)
    s = np.sin(angle)
    Rx = np.array([[1,  0, 0, 0],
                   [0,  c, s, 0],
                   [0, -s, c, 0],
                   [0,  0, 0, 1]])
    return Rx


def rotate_y(angle):
    """Returns a 3D rotation matrix about the y-axis."""
    c = np.cos(angle)
    s = np.sin(angle)
    Ry = np.array([[c, 0, -s, 0],
                   [0, 1,  0, 0],
                   [s, 0,  c, 0],
                   [0, 0,  0, 1]])
    return Ry


def rotate_z(angle):
    """Returns a 3D rotation matrix about the z-axis."""
    c = np.cos(angle)
    s = np.sin(angle)
    Rz = np.array([[ c, s, 0, 0],
                   [-s, c, 0, 0],
                   [ 0, 0, 1, 0],
                   [ 0, 0, 0, 1]])
    return Rz


# def draw_mesh(V, A, color="gray30"):
#     """Draws a mesh given its vertices and adjacency matrix."""    
#     # Draw the vertices.
#     plot_turtle.penup()
#     plot_turtle.color("gray30")
#     plot_turtle.pensize(7)
    
#     rows, cols = V.shape
    
#     for j in range(cols):
#         plot_turtle.goto(V[0:2, j])
#         plot_turtle.dot()

#     # Draw the edges.
#     plot_turtle.penup()
#     plot_turtle.color("gray30")
#     plot_turtle.pensize(2)
    
#     for j in range(cols):
#         for i in range(j, cols):
#             if A[i, j] == 1:
#                 plot_turtle.goto(V[0:2, j])
#                 plot_turtle.pendown()
#                 plot_turtle.goto(V[0:2, i])
#                 plot_turtle.penup()


def draw_wireframe(V, E, color="gray30"):
    """Draws a 3D wireframe given an object's vertices and edges."""
    # Draw the vertices.
    plot_turtle.penup()
    plot_turtle.color(color)
    plot_turtle.pensize(7)
    
    rows, cols = V.shape
    
    for j in range(cols):
        plot_turtle.goto(V[:2, j])
        plot_turtle.dot()
    
    # Draw the edges.
    plot_turtle.penup()
    plot_turtle.color(color)
    plot_turtle.pensize(2)
    
    for j in range(cols):
        root = V[:, j]
        neighbors = E[j]
        for n in neighbors:
            neighbor = V[:, n]
            plot_turtle.penup()
            plot_turtle.goto(root[:2])
            plot_turtle.pendown()
            plot_turtle.goto(neighbor[:2])


def draw_quad(V, stroke="gray30", fill="gray30"):
    """Draws a quadrilateral."""
    screen = Screen()
    screen.colormode(255)
    plot_turtle.penup()
    plot_turtle.goto(V[:2, 0])
    plot_turtle.pendown()
    plot_turtle.pencolor(stroke)
    plot_turtle.pensize(1)
    plot_turtle.fillcolor(fill)
    plot_turtle.begin_fill()
    plot_turtle.begin_poly()
    for i in range(4):
        plot_turtle.goto(V[:2, i])
    plot_turtle.goto(V[:2, 0])
    plot_turtle.end_poly()
    plot_turtle.end_fill()
    plot_turtle.penup()


def normalize(a):
    """Normalizes the values in an array."""
    a_min = np.min(a)
    a_max = np.max(a)
    a_range = a_max - a_min
    a_n = (a - a_min) / a_range
    return a_n


def get_corners(M, i, j):
    """Gets the four values surrounding a grid cell."""
    m0 = M[i, j]         # top-left
    m1 = M[i + 1, j]     # bottom-left
    m2 = M[i + 1, j + 1] # bottom-right
    m3 = M[i, j + 1]     # top-right
    return m0, m1, m2, m3


def get_vertices(X, Y, Z, i, j):
    """Returns the homogeneous coordinates of the face's vertices."""
    x0, x1, x2, x3 = get_corners(X, i, j)
    y0, y1, y2, y3 = get_corners(Y, i, j)
    z0, z1, z2, z3 = get_corners(Z, i, j)
    V = np.array([[x0, x1, x2, x3],
                  [y0, y1, y2, y3],
                  [z0, z1, z2, z3],
                  [ 1,  1,  1,  1]])
    return V


I4 = np.eye(4) # 4 x 4 identity matrix


def plot_surface(X, Y, Z, A=I4):
    """Plots a 3D surface with a given transformation."""
    tracer(0)
    
    # Get the number of rows/columns.
    N = X.shape[0]
    # Color-code each vertex.
    C = 255 * normalize(Z)
    for i in range(N - 1):
        for j in range(N - 1):
            # Get the face's vertex coordinates.
            V = get_vertices(X, Y, Z, i, j)
            # Change the basis for drawing.
            V = A @ V
            # Compute the face's average color.
            c = get_corners(C, i, j)
            c = int(np.sum(c) / 4)
            color = (c, c, c)
            # Draw the face.
            draw_quad(V, color, color)
            #draw_quad(V)
    
    tracer(1)


