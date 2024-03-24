from math import sqrt

# If the linear equation is ax + by + c = 0, the distance of the
# point A = [x,y] from the line is obtained from the following equation
def from_point(variables:list, x:int,  y:int) -> str:
  a, b, c = variables
  result = abs(a*x + b*y + c) / sqrt((a ** 2) + (b ** 2))
  return f"distance point from line is : {result}"

# distance line from origin
def from_origin(variables:list) -> str:
  a, b, c = variables
  result = abs(c) / sqrt((a ** 2) + (b ** 2))
  return f"distance origin from line is : {result}"

# If two lines are parallel, their equation can be written
# so that a and b are the same in both. That is, ax + by + c = 0 and ax + by + c' = 0
# and this function find distance two parallel lines
def two_parallel_lines(variables:list, c2:int) -> str:
  a, b, c = variables
  result = abs(c - c2) / sqrt((a ** 2) + (b ** 2))
  return f"distance of two parallel lines is : {result}"

# find the equation of a line passing through the middle of two lines
def middle_two_parallel_lines(variables:list, c2:int) -> str:
  a, b, c = variables
  c_result = (c + c2) / 2
  return f"The equation of the line passing through the middle of these two lines is: {a}x + {b}y + {c_result} = 0"
