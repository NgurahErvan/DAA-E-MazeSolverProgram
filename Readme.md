# MazeSolverProgram
Team : 
1. I Gusti Ngurah Ervan Juli Ardana (5025211205) 
2. Made Nanda Wija Vahindra (5025211160)
3. I Gusti Agung Ngurah Adhi Sanjaya (5025211056)

This is our python program that implement BFS to find a shortest path from a maze.

For the quiz 2 project, we decided to create a program that implement BFS
algorithm to solve a maze problem. This program aims to get the shortest path
possible from a maze by initiating the start position and the destination.
So, this is the final GUI design of the Maze Solve Program code implementation

So this program works by inputting the starting point coordinates and destination
point coordinates and will search the closest path to the destination point using
BFS algorithm. This program cannot run if the destination point coordinates are in
the white box, but if the starting point coordinates are in the white box it can still
run.

we define two classes named “Grid_position” and “Node”
This class is used to represent position in the maze grid and the node that
is used in the search algorithm containing position, cost, and a reference
to its parent node.

https://github.com/NgurahErvan/DAA-E-MazeSolverProgram/blob/0ed2516feb8545efbe01cbbff030627a323b8e45/mazesolve.py#L5-L15

function is bfs that implements Breadth-first Search algorithm to
find the shortest path from the start position into the destination in the
maze that we have declared in the main function. The function takes 3
inputs : grid, destination, and starting position.
https://github.com/NgurahErvan/DAA-E-MazeSolverProgram/blob/0ed2516feb8545efbe01cbbff030627a323b8e45/mazesolve.py#L18-L60  

function is bfs that implements Breadth-first Search algorithm to
find the shortest path from the start position into the destination in the
maze that we have declared in the main function. The function takes 3
inputs : grid, destination, and starting position.
https://github.com/NgurahErvan/DAA-E-MazeSolverProgram/blob/0ed2516feb8545efbe01cbbff030627a323b8e45/mazesolve.py#L63-L68 

Function draw_path is used to draw the shortest path on the canvas. it will
create an oval shape filled with blue and show according to the path found.
https://github.com/NgurahErvan/DAA-E-MazeSolverProgram/blob/0ed2516feb8545efbe01cbbff030627a323b8e45/mazesolve.py#L71-L74 

solve_maze function, it takes 4 inputs: start(x,y) and destination(x,y).
The first thing we do is declare the maze shape with an array. 1 for the
pathway and 0 for the blocked way. After that we declare destination,
starting_position, and visited blocks.
https://github.com/NgurahErvan/DAA-E-MazeSolverProgram/blob/0ed2516feb8545efbe01cbbff030627a323b8e45/mazesolve.py#L77-L149  
if the visited_blocks is found we print the amount of shortest path steps,
and the shortest path itself into the terminal.Then create a GUI using tk design as we show above. 
There is a solve button, it's used to solve the input that is given by the user
in the input box in GUI to run the solve_maze function. A new canvas
where the maze grid and the shortest path will be displayed. if there are no results in visited_blocks the program will print “Path does
not exist” in the terminal.
in the main function we defined the initial value of x and y from the starting
position and destination to 0. The main function is calling the solve_maze  
 
So this program works by inputting the starting point coordinates and destination
point coordinates and will search the closest path to the destination point using
BFS algorithm. This program cannot run if the destination point coordinates are in
the white box, but if the starting point coordinates are in the white box it can still
run.
  
So, this is the example implementation of this program. The starting point is at X
= 11, Y = 0n coordinates and the destination point is at X= 1, Y = 10. The X
coordinate will represent the vertical path and the Y coordinate will represent the
horizontal path. The range of the coordinate start from 0 to 11 on each
coordinate.


