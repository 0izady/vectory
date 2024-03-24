# Symmetry of point a to b
def point_to_point(a:list,b:list) -> str:
  x = 2 * int(b[0]) - int(a[0]) # 2a - x
  y = 2 * int(b[1]) - int(a[1]) # 2b - y
  return f"Correlation of point A to point M: [{x},{y}]"

# Symmetry to the y axis
def y_axis(x:int,y:int) -> str:
  return f"The relation of point A to the y axis becomes: [{x},{-y}]"

# Symmetry to the x axis
def x_axis(x:int,y:int) -> str:
  return f"The relation of point A to the x axis becomes: [{-x},{y}]"

# Symmetry to the origin of coordinates
def origin(x:int,y:int) -> str:
  return f"The relation of point A to the coordinate origin axis becomes: [{-x},{-y}]"

# Symmetry to the first and third halves
def first_third_halves(x:int,y:int) -> str:
  return f"The relation of point A to the first and third halves axis becomes: [{y},{x}]"

# Symmetry to the second and fourth halves
def second_fourth_halves(x:int,y:int) -> str:
  return f"The relation of point A to the second and fourth halves axis becomes: [{-y},{-x}]"
