import re
from sympy import symbols, Eq, solve
import matplotlib.pyplot as plt
import numpy as np


def extract_coefficients(equation):
    # Use regular expressions to find coefficients
    # The regex now handles optional spaces and coefficients of 1 or -1
    matches = re.findall(
        r'([+-]?\d*)\s*\*\s*x\s*([+-]?\d*)\s*\*\s*y\s*=\s*([+-]?\d+)', equation.replace(' ', ''))

    if matches:
        a, b, c = matches[0]
        a = int(a) if a not in ['', '+'] else 1
        b = int(b) if b not in ['', '+'] else 1
        c = int(c)
        return a, b, c
    else:
        return "The input equation is not in the correct format."

# find intersection of two line
# equations form example : 2 * x + 3 * y = 7 => (2x + 3y = 7)
def intersection(equation1: str, equation2: str) -> str:
  a1, b1, c1 = extract_coefficients(equation1)
  a2, b2, c2 = extract_coefficients(equation2)

  x, y = symbols('x y')

  eq1 = Eq(a1 * x + b1 * y, c1)
  eq2 = Eq(a2 * x + b2 * y, c2)

  # Solve the equations
  solution = solve((eq1, eq2), (x, y))

  return f"The coordinates of the point are [{solution[x]},{solution[y]}]."


# show intersection of two line
def show_intersection(m1: int, m2: int, h1: int, h2: int) -> str:
    x = np.linspace(-10, 10, 500)

    plt.plot(x, x * m1 + h1, 'red')
    plt.plot(x, x * m2 + h2, 'green')

    xi = (h1 - h2) / (m2 - m1)
    yi = m1 * xi + h1

    plt.axvline(x=xi, color='gray', linestyle='--')
    plt.axhline(y=yi, color='gray', linestyle='--')

    plt.scatter(xi, yi, color='black')

    plt.show()

# finde line slope of two line
def line_slope(a: list, b: list) -> str:
    x1, y1 = a
    x2, y2 = b
    line_slope = (y1 - y2) / (x1 - x2)
    return f"line slope of the two line is : {line_slope}"
