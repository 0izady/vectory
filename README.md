# vectory
Performing calculations and linear equations with Python

## Install and run
for install project : `git clone https://github.com/Qprimee/vectory.git`

go to project : `cd vectory`

run project : `python3 vectory.py`

## Command List:
      
`help` - Show this help message     
      
calculations 
      
`show_vector(m,h)` - show represents a linear equation in a coordinate vector.
M is line slope and H is width from the origin  
      
`get_line_slope(x,y,h)` - finde line slope 
X is the length, Y is the width and H is width from the origin
      
`get_width_origin(x,y,m)` - find width origin     
X is the length, Y is the width and M is line slope    
      
`get_length_origin(m,h)` - find lenght origin     
M is line slope and H is width from the origin  
      
`middle_line(a,b)` - find the coordinates of the middle of the line segment   
A is the coordinate of the first point and B is the coordinate of the second point 
      
symmetry     
      
`symmetry:point_to_point(a,b)` - Symmetry of point a to b
A is the coordinate of the first point and B is the coordinate of the second point 
      
`symmetry:y_axis(x,y)` - Symmetry to the y axis   
X is the length of the point and Y is the width of the point  
      
`symmetry:x_axis(x,y)` - Symmetry to the x axis   
X is the length of the point and Y is the width of the point  
      
`symmetry:origin(x,y)` - Symmetry to the origin of coordinates  
X is the length of the point and Y is the width of the point  
      
`symmetry:first_third_halves(x,y)` - Symmetry to the first and third halves   
X is the length of the point and Y is the width of the point  
      
`symmetry:second_fourth_halves(x,y)` - Symmetry to the second and fourth halves      
X is the length of the point and Y is the width of the point  
      
distance     
      
`distance:two_point(a,b)` - find distance from point a to b     
A is the coordinate of the first point and B is the coordinate of the second point 
      
`distance:origin(x,y)` - find distance from point a to coordinate origin      
X is the length of the point and Y is the width of the point  
      
`distance:dividing_point(a,b,n,m)` - find the dividing point of the line segment into equal proportions   
A and B are the coordinates of two points that are divided according to N and M    
      
intersection 
      
`intersection:intersection(equation1,equation2)` - find intersection of two line     
equation1 is first and equation2 is secend equation like: 2 * x + -6 * y = 7
      
`intersection:show_intersection(m1,m2,c1,c2)` - show intersection of two line 
M1 and M2 are line slopes and H1 and H2 are width from the origin    
      
`intersection:line_slope(a,b)` - finde line slope of two line   
A is the coordinate of the first point and B is the coordinate of the second point 
      
checking     
      
`checking:aligned_three_point(a,b,c)` - check a,b and c points is aligned     
A is the coordinate of the first point , B is the coordinate of the second point and C is the coordinate of    
 the third point    
      
`checking:two_parallel_lines(m1,m2)` - check two line is parallel      
M1 and M2 are line slopes  
      
`checking:two_parallel_lines(m1,m2)` - check two line is perpendicular 
M1 and M2 are line slopes  
      
`checking:matching_two_lines(a,b)` - check two line is matching 
A is the coordinate of the first point and B is the coordinate of the second point 
      
line symmetry
      
`line_symmetry:y_axis(equation)` - Symmetry line to the y axis  
equation is equation like: 2 * x + -6 * y = 7   
      
`line_symmetry:x_axis(equation)` - Symmetry line to the x axis  
equation is equation like: 2 * x + -6 * y = 7   
      
`line_symmetry:origin(equation)` - Symmetry line to the origin of coordinates 
equation is equation like: 2 * x + -6 * y = 7   
      
`line_symmetry:first_third_halves(equation)` - Symmetry line to the first and third halves  
equation is equation like: 2 * x + -6 * y = 7   
      
`line_symmetry:second_fourth_halves(equation)` - Symmetry line to the second and fourth halves     
equation is equation like: 2 * x + -6 * y = 7   
      
line distance
      
`line_distance:from_point(variables, x, y)` - If the linear equation is ax + by + c = 0, the distance of the     
point A =  from the line is obtained from the following equation     
variables is a,b,c like: (1,2,3), X is the length of the point and Y is the width of the point   
      
`line_distance:from_origin(variables)` - distance line from origin     
variables is a,b,c like: (1,2,3)  
      
`line_distance:two_parallel_lines(variables, c2)` - If two lines are parallel, their equation can be written     
so that a and b are the same in both. That is, ax + by + c = 0 and ax + by + c' = 0
and this function find distance two parallel lines     
variables is a,b,c like: (1,2,3) and C2 is c'   
      
`line_distance:middle_two_parallel_lines(variables, c2)` - find the equation of a line passing through the
middle of two lines
variables is a,b,c like: (1,2,3) and C2 is c'   

`exit` - Exit the program    

> [!NOTE]
> for run command just type name of command for example distance:dividing_point and then in some input we get  
> a,b,n and m 
 
> [!NOTE]
> all X, Y, M and H inputs must be int and all A and B is list like (2,4)
