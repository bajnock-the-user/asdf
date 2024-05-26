from collections import deque

def read_maze(filename):
    with open(filename, 'r') as file:
        lines = file.read().strip().split('\n')
    
    mazes = []
    maze = []
    for line in lines:
        if line.strip().startswith("A"):
            if maze:
                mazes.append(maze)
            maze = []
        elif line.strip():
            maze.append(list(line.strip()))
    if maze:
        mazes.append(maze)
    return mazes

def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [])])
    visited = set()
    visited.add(start)

    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    while queue:
        (current_x, current_y), path = queue.popleft()
        
        if (current_x, current_y) == goal:
            return path + ['G']

        for direction, (dx, dy) in directions.items():
            next_x, next_y = current_x + dx, current_y + dy

            if 0 <= next_x < rows and 0 <= next_y < cols and maze[next_x][next_y] != '#' and (next_x, next_y) not in visited:
                queue.append(((next_x, next_y), path + [direction]))
                visited.add((next_x, next_y))
    return []

def solve_maze(maze):
    start = None
    goal = None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'G':
                goal = (i, j)
    
    if not start or not goal:
        return "No start or goal found in the maze"

    path = bfs(maze, start, goal)
    return ['S'] + path

def print_solution(maze_label, solution):
    print(maze_label)
    if solution:
        print(' '.join(solution))
    else:
        print("No solution found")
