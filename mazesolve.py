from collections import deque
import tkinter as tk


class Grid_Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Node:
    def __init__(self, pos: Grid_Position, cost, parent=None):
        self.pos = pos
        self.cost = cost
        self.parent = parent


def bfs(Grid, dest: Grid_Position, start: Grid_Position):
    adj_cell_x = [-1, 0, 0, 1]
    adj_cell_y = [0, -1, 1, 0]
    m, n = (len(Grid), len(Grid))
    visited_blocks = [[False for i in range(m)] for j in range(n)]
    visited_blocks[start.x][start.y] = True
    queue = deque()
    sol = Node(start, 0)
    queue.append(sol)
    cells = 4
    cost = 0
    while queue:
        current_block = queue.popleft()
        current_pos = current_block.pos
        if current_pos.x == dest.x and current_pos.y == dest.y:
            print("Algorithm used = BFS")
            print("Path found!!")
            print("Total nodes visited = ", cost)
            return current_block

        if current_block not in visited_blocks:
            visited_blocks[current_pos.x][current_pos.y] = True
            cost = cost + 1
        x_pos = current_pos.x
        y_pos = current_pos.y
        for i in range(cells):
            if x_pos == len(Grid) - 1 and adj_cell_x[i] == 1:
                x_pos = current_pos.x
                y_pos = current_pos.y + adj_cell_y[i]
            if y_pos == 0 and adj_cell_y[i] == -1:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y
            else:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y + adj_cell_y[i]
            if x_pos < 12 and y_pos < 12 and x_pos >= 0 and y_pos >= 0:
                if Grid[x_pos][y_pos] == 1:
                    if not visited_blocks[x_pos][y_pos]:
                        next_cell = Node(Grid_Position(x_pos, y_pos),
                                         current_block.cost + 1, parent=current_block)
                        visited_blocks[x_pos][y_pos] = True
                        queue.append(next_cell)
    return None


def create_grid(maze, canvas):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            color = 'white' if maze[i][j] == 0 else 'black'
            canvas.create_rectangle(
                j * 30, i * 30, (j + 1) * 30, (i + 1) * 30, fill=color)


def draw_path(path, canvas):
    for pos in path:
        canvas.create_oval(pos.y * 30 + 10, pos.x * 30 + 10,
                           (pos.y + 1) * 30 - 10, (pos.x + 1) * 30 - 10, fill='blue')


def solve_maze():
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    destination = Grid_Position(10, 6)
    starting_position = Grid_Position(11, 10)
    visited_blocks = bfs(maze, destination, starting_position)

    if visited_blocks is not None:
        print("Shortest path steps = ", visited_blocks.cost)
        path = []
        while visited_blocks.parent is not None:
            path.append(visited_blocks.pos)
            visited_blocks = visited_blocks.parent
        path.append(starting_position)
        path.reverse()
        print("Shortest path:")
        for pos in path:
            print(f"({pos.x}, {pos.y})")

        # Create GUI
        root = tk.Tk()
        root.title("Maze Solver")
        canvas = tk.Canvas(root, width=360, height=360)
        canvas.pack()
        create_grid(maze, canvas)
        draw_path(path, canvas)
        tk.mainloop()
    else:
        print("Path does not exist")


if __name__ == '__main__':
    print("main start\n")
    solve_maze()
