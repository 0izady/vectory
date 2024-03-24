import math
import numpy as np

# find distance from point a to b
# AB lien be : sqrt((y2 - y1)**2 + (x2-x1)**2)
def two_point(a:list,b:list) -> str:
  x = (int(a[1]) - int(b[0])) ** 2
  y = (int(a[1]) - int(b[0])) ** 2
  result = math.sqrt(y + x)
  return f"Distance from point a to b: {result}"

# find distance from point a to coordinate origin
# OA line be : sqrt(x**2 + y**2)
def origin(x:int, y:int) -> str:
  x **= 2
  y **= 2
  result = math.sqrt(x + y)
  return f"Distance from point a to origin: {result}"

# find the dividing point of the line segment into equal proportions
# M = (n * [A]) + (m * [B]) / (n + m)
def dividing_point(a:list,b:list,n:int,m:int) -> str:
  first_point = np.dot(n,a)
  secend_point = np.dot(m,b)
  result = (first_point + secend_point) / (n+m)
  return f"If the point M divides the line segment AB in the ratio of m to n, the coordinates of M are as follows: {result}"
