import re

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

# Symmetry to the y axis
def y_axis(equation:str) -> str:
    a, b, c = extract_coefficients(equation)
    return f"The relation of line to the y axis becomes: {a}x + {-1*b}y = {c}"

# Symmetry to the x axis
def x_axis(equation:str) -> str:
    a, b, c = extract_coefficients(equation)
    return f"The relation of line to the x_axis becomes: {-1 * a}x + {b}y = {c}"

# Symmetry to the origin of coordinates
def origin(equation:str) -> str:
    a, b, c = extract_coefficients(equation)
    return f"The relation of line to the origin becomes: {-1 * a}x + {-1 * b}y = {c}"

# Symmetry to the first and third halves
def first_third_halves(equation:str) -> str:
    a, b, c = extract_coefficients(equation)
    return f"The relation of line to the first_third_halves becomes: {b}x + {a}y = {c}"

# Symmetry to the second and fourth halves
def second_fourth_halves(equation:str) -> str:
    a, b, c = extract_coefficients(equation)
    return f"The relation of line to the first_third_halves becomes: {-1 * b}x + {-1 * a}y = {c}"
