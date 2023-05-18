from collections import deque

class Grid_Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Node:
    def __init__(self, pos: Grid_Position, cost, parent=None):
        self.pos = pos
        self.cost = cost
        self.parent = parent
        
def main():
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
    else:
        print("Path does not exist")

if __name__ == '__main__':
    print("main start\n")
    main()

