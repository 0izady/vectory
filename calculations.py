import matplotlib.pyplot as plt
import numpy as np

# m is line slope and h is width from the origin
# this func show represents a linear equation in a coordinate vector
def show_vector(m:int, h:int) -> str:
  # Generate x values
  x = np.linspace(-10, 10, 100)

  # Calculate corresponding y values
  y = m*x + h

  # Plot the line
  plt.plot(x, y, label=f"y = {m}x + {h}")
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title(f"Linear Equation: y = {m}x + {h}")
  plt.grid(True)
  plt.legend()
  plt.show()

# in this(y = mx + h) we find m
def get_line_slope(x:int, y:int, h:int) -> str:
  m = (y-h)/x
  return f"Your linear equation is: y = {m}x + {h}"

# in this(y = mx + h) we find h
def get_width_origin(x:int, y:int, m:int) -> str:
  h = y - m * x
  return f"Your linear equation is: y = {m}x + {h}"

# To find the length from the origin, we set y equal to zero and solve the equation
# y = mx + h => 0 = mx + h => mx = -h => x = -h / m
def get_length_origin(m:int,h:int):
  length_origin = -h/m
  return f"Length from the origin of this line:{length_origin}"

# In this function, we find the coordinates of the middle of the line segment
# of line a and b.(we get array)
# example of a , b and output is [x,y]
def middle_line(a:list, b:list) -> str:
  x = int(a[0]) + int(b[0])
  y = int(a[1]) + int(b[1])
  return f"The coordinates of the middle of the line segment of a and b are: [{x},{y}]"
