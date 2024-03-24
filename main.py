from rich.theme import Theme
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich import print
import os
import calculations,distance,symmetry,intersection,check,line_symmetry,line_distance

console = Console(theme=Theme({"repr.number": "bold green blink"}),style="blue")
error_console = Console(stderr=True, style="bold red")
console.rule("[bold blue]welcome to Vectory")
command = ""

def convert_to_array(tuple_string):
    # Remove the parentheses
    tuple_string = tuple_string.strip('()')
    # Split the string by comma and convert each number to an integer
    array = [int(num) for num in tuple_string.split(',')]
    return array
def help():
    help_text = """
      [b]Command List:[/b]

      [green]help[/green] - Show this help message

      [bold red]calculations[/]

      [green]show_vector(m,h)[/green] - show represents a linear equation in a coordinate vector.
      [yellow]M is line slope and H is width from the origin[/]

      [green]get_line_slope(x,y,h)[/green] - finde line slope
      [yellow]X is the length, Y is the width and H is width from the origin[/]

      [green]get_width_origin(x,y,m)[/green] - find width origin
      [yellow]X is the length, Y is the width and M is line slope [/]

      [green]get_length_origin(m,h)[/green] - find lenght origin
      [yellow]M is line slope and H is width from the origin[/]

      [green]middle_line(a,b)[/green] - find the coordinates of the middle of the line segment
      [yellow]A is the coordinate of the first point and B is the coordinate of the second point[/]

      [bold red]symmetry[/]

      [green]symmetry:point_to_point(a,b)[/green] - Symmetry of point a to b
      [yellow]A is the coordinate of the first point and B is the coordinate of the second point[/]

      [green]symmetry:y_axis(x,y)[/green] - Symmetry to the y axis
      [yellow]X is the length of the point and Y is the width of the point[/]

      [green]symmetry:x_axis(x,y)[/green] - Symmetry to the x axis
      [yellow]X is the length of the point and Y is the width of the point[/]

      [green]symmetry:origin(x,y)[/green] - Symmetry to the origin of coordinates
      [yellow]X is the length of the point and Y is the width of the point[/]

      [green]symmetry:first_third_halves(x,y)[/green] - Symmetry to the first and third halves
      [yellow]X is the length of the point and Y is the width of the point[/]

      [green]symmetry:second_fourth_halves(x,y)[/green] - Symmetry to the second and fourth halves
      [yellow]X is the length of the point and Y is the width of the point[/]

      [bold red]distance[/]

      [green]distance:two_point(a,b)[/green] - find distance from point a to b
      [yellow]A is the coordinate of the first point and B is the coordinate of the second point[/]

      [green]distance:origin(x,y)[/green] - find distance from point a to coordinate origin
      [yellow]X is the length of the point and Y is the width of the point[/]

      [green]distance:dividing_point(a,b,n,m)[/green] - find the dividing point of the line segment into equal proportions
      [yellow]A and B are the coordinates of two points that are divided according to N and M[/]

      [bold red]intersection[/]

      [green]intersection:intersection(equation1,equation2)[/green] - find intersection of two line
      [yellow]equation1 is first and equation2 is secend equation like: 2 * x + -6 * y = 7[/]

      [green]intersection:show_intersection(m1,m2,c1,c2)[/green] - show intersection of two line
      [yellow]M1 and M2 are line slopes and H1 and H2 are width from the origin[/]

      [green]intersection:line_slope(a,b)[/green] - finde line slope of two line
      [yellow]A is the coordinate of the first point and B is the coordinate of the second point[/]

      [bold red]checking[/]

      [green]checking:aligned_three_point(a,b,c)[/green] - check a,b and c points is aligned
      [yellow]A is the coordinate of the first point , B is the coordinate of the second point and C is the coordinate of the third point[/]

      [green]checking:two_parallel_lines(m1,m2)[/green] - check two line is parallel
      [yellow]M1 and M2 are line slopes[/]

      [green]checking:two_parallel_lines(m1,m2)[/green] - check two line is perpendicular
      [yellow]M1 and M2 are line slopes[/]

      [green]checking:matching_two_lines(a,b)[/green] - check two line is matching
      [yellow]A is the coordinate of the first point and B is the coordinate of the second point[/]

      [bold red]line symmetry[/]

      [green]line_symmetry:y_axis(equation)[/green] - Symmetry line to the y axis
      [yellow]equation is equation like: 2 * x + -6 * y = 7[/]

      [green]line_symmetry:x_axis(equation)[/green] - Symmetry line to the x axis
      [yellow]equation is equation like: 2 * x + -6 * y = 7[/]

      [green]line_symmetry:origin(equation)[/green] - Symmetry line to the origin of coordinates
      [yellow]equation is equation like: 2 * x + -6 * y = 7[/]

      [green]line_symmetry:first_third_halves(equation)[/green] - Symmetry line to the first and third halves
      [yellow]equation is equation like: 2 * x + -6 * y = 7[/]

      [green]line_symmetry:second_fourth_halves(equation)[/green] - Symmetry line to the second and fourth halves
      [yellow]equation is equation like: 2 * x + -6 * y = 7[/]

      [bold red]line distance[/]

      [green]line_distance:from_point(variables, x, y)[/green] - If the linear equation is ax + by + c = 0, the distance of the
      point A = [x,y] from the line is obtained from the following equation
      [yellow]variables is a,b,c like: (1,2,3), X is the length of the point and Y is the width of the point[/]

      [green]line_distance:from_origin(variables)[/green] - distance line from origin
      [yellow]variables is a,b,c like: (1,2,3)[/]

      [green]line_distance:two_parallel_lines(variables, c2)[/green] - If two lines are parallel, their equation can be written
      so that a and b are the same in both. That is, ax + by + c = 0 and ax + by + c' = 0
      and this function find distance two parallel lines[/]
      [yellow]variables is a,b,c like: (1,2,3) and C2 is c'[/]

      [green]line_distance:middle_two_parallel_lines(variables, c2)[/green] - find the equation of a line passing through the middle of two lines
      [yellow]variables is a,b,c like: (1,2,3) and C2 is c'[/]

      # for run command just type name of command for example distance:dividing_point and then in some input we get
       a,b,n and m

      # all X, Y, M and H inputs must be int and all A and B is list like (2,4)

      [green]exit[/green] - Exit the program
    """
    panel = Panel(help_text, title="Help", style="blue")
    print(panel)
def get_input(command):
    command = command.lower()
    if command == "help":
        help()
    # calculations
    elif command == "show_vector":
        try:
            line_slope = int(Prompt.ask("Enter line slope", default=0))
            width_from_origin = int(Prompt.ask("Enter width from the origin", default=0))
            console.print(calculations.show_vector(line_slope,width_from_origin))
        except ValueError:
            error_console.print("inputs must be int")

    elif command == "get_line_slope":
        try:
            length = int(Prompt.ask("Enter line length(x)", default=0))
            width = int(Prompt.ask("Enter line width(h)", default=0))
            width_from_origin = int(Prompt.ask("Enter width from the origin", default=0))
            console.print(calculations.get_line_slope(length,width,width_from_origin))
        except ValueError:
            error_console.print("inputs must be int")
    elif command == "get_width_origin":
        try:
            length = int(Prompt.ask("Enter line length(x)", default=0))
            width = int(Prompt.ask("Enter line width(h)", default=0))
            line_slope = int(Prompt.ask("Enter line slope", default=0))
            console.print(calculations.get_width_origin(length,width,line_slope))
        except ValueError:
            error_console.print("inputs must be int")
    elif command == "get_length_origin":
        try:
            line_slope = int(Prompt.ask("Enter line slope", default=0))
            width_from_origin = int(Prompt.ask("Enter width from the origin", default=0))
            console.print(calculations.get_length_origin(line_slope,width_from_origin))
        except ValueError:
            error_console.print("inputs must be int")
    elif command == "middle_line":
        try:
            first_point = convert_to_array(
                Prompt.ask("Enter coordinate of the first point", default="(1,2)")
            )
            secend_point = convert_to_array(
                Prompt.ask("Enter coordinate of the secend point", default="(1,2)")
            )
            console.print(calculations.middle_line(first_point,secend_point))
        except ValueError:
            error_console.print("The input equation is not in the correct format.")
    # distance
    elif command == "distance:two_point":
        try:
            first_point = convert_to_array(
                Prompt.ask("Enter coordinate of the first point", default="(1,2)")
            )
            secend_point = convert_to_array(
                Prompt.ask("Enter coordinate of the secend point", default="(1,2)")
            )
            console.print(distance.two_point(first_point,secend_point))
        except ValueError:
            error_console.print("The input equation is not in the correct format.")
    elif command == "distance:origin":
        try:
            length = int(Prompt.ask("Enter line length(x)", default=0))
            width = int(Prompt.ask("Enter line width(h)", default=0))
            console.print(distance.origin(length,width))
        except ValueError:
            error_console.print("inputs must be int")
    elif command == "distance:dividing_point":
        try:
            first_point = convert_to_array(
                Prompt.ask("Enter coordinate of the first point", default="(1,2)")
            )
            secend_point = convert_to_array(
                Prompt.ask("Enter coordinate of the secend point", default="(1,2)")
            )
            divided_n = int(Prompt.ask("Enter first ratio",default=1))
            divided_m = int(Prompt.ask("Enter secend ratio",default=1))
            console.print(distance.dividing_point(first_point,secend_point,divided_n,divided_m))
        except ValueError:
            error_console.print("The input is not in the correct format.")
    # symmetry
    elif command == "symmetry:point_to_point":
        try:
            first_point = convert_to_array(
                Prompt.ask("Enter coordinate of the first point", default="(1,2)")
            )
            secend_point = convert_to_array(
                Prompt.ask("Enter coordinate of the secend point", default="(1,2)")
            )
            console.print(symmetry.point_to_point(first_point,secend_point))
        except ValueError:
            error_console.print("The input is not in the correct format.")
    elif command == "symmetry:y_axis":
        try:
            length = int(Prompt.ask("Enter line length(x)", default=0))
            width = int(Prompt.ask("Enter line width(h)", default=0))
            console.print(symmetry.y_axis(length, width))
        except ValueError:
            error_console.print("inputs must be int")
    elif command == "symmetry:x_axis":
        try:
            length = int(Prompt.ask("Enter line length(x)", default=0))
            width = int(Prompt.ask("Enter line width(h)", default=0))
            console.print(symmetry.x_axis(length, width))
        except ValueError:
            error_console.print("inputs must be int")
    elif command == "symmetry:origin":
        try:
            length = int(Prompt.ask("Enter line length(x)", default=0))
            width = int(Prompt.ask("Enter line width(h)", default=0))
            console.print(symmetry.origin(length, width))
        except ValueError:
            error_console.print("inputs must be int")
    elif command =="symmetry:first_third_halves":
        try:
            length = int(Prompt.ask("Enter line length(x)", default=0))
            width = int(Prompt.ask("Enter line width(h)", default=0))
            console.print(symmetry.first_third_halves(length, width))
        except ValueError:
            error_console.print("inputs must be int")
    elif command == "symmetry:second_fourth_halves":
        try:
            length = int(Prompt.ask("Enter line length(x)", default=0))
            width = int(Prompt.ask("Enter line width(h)", default=0))
            console.print(symmetry.second_fourth_halves(length, width))
        except ValueError:
            error_console.print("inputs must be int")
    # intersection
    elif command == "intersection:intersection":
        try:
            equation1 = Prompt.ask("Enter first equation", default="2 * x + 3 * y = 4")
            equation2 = Prompt.ask("Enter secend equation", default="2 * x + 3 * y = 4")
            console.print(intersection.intersection(equation1,equation2))
        except:
            error_console.print("The input equation is not in the correct format.")
    elif command == "intersection:show_intersection":
        try:
            line_slope1 = int(Prompt.ask("Enter first line slope", default=0))
            line_slope2 = int(Prompt.ask("Enter secend line slope", default=0))
            width_from_origin1 = int(Prompt.ask("Enter first width from origin", default=0))
            width_from_origin2 = int(Prompt.ask("Enter secend width from origin", default=0))
            console.print(intersection.show_intersection(
                line_slope1,line_slope2,
                width_from_origin1,width_from_origin2
            ))
        except ValueError:
            error_console.print("inputs must be int")
    elif command == "intersection:line_slope":
        try:
            first_point = convert_to_array(
                Prompt.ask("Enter coordinate of the first point", default="(1,2)")
            )
            secend_point = convert_to_array(
                Prompt.ask("Enter coordinate of the secend point", default="(1,2)")
            )
            console.print(intersection.line_slope(first_point,secend_point))
        except:
            error_console.print("The input equation is not in the correct format.")
    elif command == "checking:aligned_three_point":
        try:
            first_point = convert_to_array(
                Prompt.ask("Enter coordinate of the first point", default="(1,2)")
            )
            secend_point = convert_to_array(
                Prompt.ask("Enter coordinate of the secend point", default="(1,2)")
            )
            third_point = convert_to_array(
                Prompt.ask("Enter coordinate of the third point", default="(1,2)")
            )
            console.print(check.aligned_three_point(first_point,secend_point,third_point))
        except:
            error_console.print("The input equation is not in the correct format.")
    elif command == "checking:two_parallel_lines":
        try:
            line_slope1 = int(Prompt.ask("Enter first line slope", default=0))
            line_slope2 = int(Prompt.ask("Enter secend line slope", default=0))
            console.print(check.two_parallel_lines(line_slope1,line_slope2))
        except:
            error_console.print("inputs must be int")
    elif command == "checking:two_perpendicular_lines":
        try:
            line_slope1 = int(Prompt.ask("Enter first line slope", default=0))
            line_slope2 = int(Prompt.ask("Enter secend line slope", default=0))
            console.print(check.two_perpendicular_lines(line_slope1,line_slope2))
        except:
            error_console.print("inputs must be int")
    elif command == "checking:matching_two_lines":
        try:
            first_equation = convert_to_array(
                Prompt.ask("Enter coordinate of the first varibels", default="(1,2,3)")
            )
            secend_equation = convert_to_array(
                Prompt.ask("Enter coordinate of the secend equation", default="(1,2,3)")
            )
            console.print(check.matching_two_lines(first_equation, secend_equation))
        except:
            error_console.print("The input equation is not in the correct format.")
    # line_symmetry
    elif command == "line_symmetry:y_axis":
        try:
            equation = Prompt.ask("Enter the equation(a * x + b * y = c)", default="2 * x + 3 * y = 4")
            console.print(line_symmetry.y_axis(equation))
        except:
            error_console.print("The input equation is not in the correct format.")
    elif command == "line_symmetry:x_axis":
        try:
            equation = Prompt.ask("Enter the equation(a * x + b * y = c)", default="2 * x + 3 * y = 4")
            console.print(line_symmetry.x_axis(equation))
        except:
            error_console.print("The input equation is not in the correct format.")
    elif command == "line_symmetry:origin":
        try:
            equation = Prompt.ask("Enter the equation(a * x + b * y = c)", default="2 * x + 3 * y = 4")
            console.print(line_symmetry.origin(equation))
        except:
            error_console.print("The input equation is not in the correct format.")
    elif command == "line_symmetry:first_third_halves":
        try:
            equation = Prompt.ask("Enter the equation(a * x + b * y = c)", default="2 * x + 3 * y = 4")
            console.print(line_symmetry.first_third_halves(equation))
        except:
            error_console.print("The input equation is not in the correct format.")
    elif command == "line_symmetry:second_fourth_halves":
        try:
            equation = Prompt.ask("Enter the equation(a * x + b * y = c)", default="2 * x + 3 * y = 4")
            console.print(line_symmetry.second_fourth_halves(equation))
        except:
            error_console.print("The input equation is not in the correct format.")
    elif command == "line_distance:from_point":
        try:
            variables = convert_to_array(
                Prompt.ask("Enter variables(a,b and c of this equation : ax + by + c = 0)", default="(1,2,3)")
            )
            length = int(Prompt.ask("Enter line length(x)", default=0))
            width = int(Prompt.ask("Enter line width(h)", default=0))
            console.print(line_distance.from_point(variables,length,width))
        except:
             error_console.print("The input equation is not in the correct format.")
    elif command == "line_distance:from_origin":
        try:
            variables = convert_to_array(
                Prompt.ask("Enter variables(a,b and c of this equation : ax + by + c = 0)", default="(1,2,3)")
            )
            console.print(line_distance.from_origin(variables))
        except:
             error_console.print("The input equation is not in the correct format.")
    elif command == "line_distance:two_parallel_lines":
        try:
            variables = convert_to_array(
                Prompt.ask("Enter variables(a,b and c of this equation : ax + by + c = 0)", default="(1,2,3)")
            )
            secend_c = int(Prompt.ask("Enter secend c(c')", default=0))
            console.print(line_distance.two_parallel_lines(variables,secend_c))
        except:
             error_console.print("The input equation is not in the correct format.")
    elif command == "line_distance:middle_two_parallel_lines":
        try:
            variables = convert_to_array(
                Prompt.ask("Enter variables(a,b and c of this equation : ax + by + c = 0)", default="(1,2,3)")
            )
            secend_c = int(Prompt.ask("Enter secend c(c')", default=0))
            console.print(line_distance.middle_two_parallel_lines(variables,secend_c))
        except:
             error_console.print("The input equation is not in the correct format.")
    elif command == "cls":
        # for Windows
        if os.name == 'nt':
            os.system('cls')
        # for Unix/Linux/MacOS
        else:
            os.system('clear')
    else:
        error_console.print("This command is not available")

def main():
   while True:
      command = Prompt.ask("What i can do for [bold green]you[/]? :fire:", default="type help for see commands")
      if command.lower() == "exit":
         console.print("goodbye:wave:", style="magenta")
         break
      else:
         get_input(command)

if __name__ == '__main__':
    main()
