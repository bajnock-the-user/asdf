from collections import deque

def read_maze(file_path):
    with open(file_path, 'r') as file:
        maze = [list(line.strip()) for line in file]
    return maze

def find_start_and_goal(maze):
    start = None
    goal = None
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'G':
                goal = (r, c)
    return start, goal

def bfs(maze, start, goal):
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    queue = deque([(start, "")])
    visited = set()
    visited.add(start)

    while queue:
        (current_pos, path) = queue.popleft()
        
        if current_pos == goal:
            return path
        
        for direction, (dr, dc) in directions.items():
            new_row, new_col = current_pos[0] + dr, current_pos[1] + dc
            if (0 <= new_row < len(maze) and
                0 <= new_col < len(maze[0]) and
                maze[new_row][new_col] != '#' and
                (new_row, new_col) not in visited):
                queue.append(((new_row, new_col), path + direction))
                visited.add((new_row, new_col))
    return None

def solve_maze(file_path):
    maze = read_maze(file_path)
    start, goal = find_start_and_goal(maze)
    path = bfs(maze, start, goal)
    return path

if __name__ == "__main__":
    input_file = "input.txt"
    path = solve_maze(input_file)
    if path:
        print("S", end=" ")
        for move in path:
            print(move, end=" ")
        print("G")
    else:
        print("No path found")
