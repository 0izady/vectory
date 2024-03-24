# check a,b and c line is aligned
def aligned_three_point(a: list, b: list, c:list) -> str:
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    line_slope_ab = (y1 - y2) / (x1 - x2)
    line_slope_bc = (y2 - y3) / (x2 - x3)
    if line_slope_ab == line_slope_bc:
        return f"All three points are aligned"
    else:
        return f"These three points are not aligned. To align, the slope of the BC line must be equal to {line_slope_ab}"

# check two line is parallel
def two_parallel_lines(m1: int,m2: int) -> str:
    if m1 == m2:
        return f"These two lines are parallel"
    else:
        return f"These two lines are not parallel, for them to be parallel, M2 should be equal to {m1}"

# check two line is perpendicular
def two_perpendicular_lines(m1: int,m2: int) ->str:
  if m1 * m2 == -1:
      return f"These two lines are perpendicular"
  else:
      return f"These two lines are not perpendicular. For these two lines to be perpendicular, M1 must be equal to {-1/m2}"

# check two line is matching
# a(ax + by + c = 0) -> [a,b,c]
# b(ax + by + c = 0) -> [a',b',c']
# inputs like : (1,2,3)
def matching_two_lines(equation1:list,equation2:list) -> str:
  a1, b1, c1 = equation1
  a2, b2, c2 = equation2
  if (a1/a2) == (b1/b2) == (c1/c2):
      return f"These two lines coincide"
  else:
      return f"These two lines do not match"

