from collections import deque

def read_maze(file_path):
    with open(file_path, 'r') as f:
        maze = [list(line.strip()) for line in f.readlines()]
    return maze

def find_start_goal(maze):
    start = goal = None
    for r, row in enumerate(maze):
        for c, value in enumerate(row):
            if value == 'S':
                start = (r, c)
            elif value == 'G':
                goal = (r, c)
    return start, goal

def bfs(maze, start, goal):
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    queue = deque([(start, '')])
    visited = set()
    visited.add(start)

    while queue:
        (current_r, current_c), path = queue.popleft()
        
        if (current_r, current_c) == goal:
            return path
        
        for direction, (dr, dc) in directions.items():
            next_r, next_c = current_r + dr, current_c + dc
            
            if 0 <= next_r < len(maze) and 0 <= next_c < len(maze[0]):
                if maze[next_r][next_c] != '#' and (next_r, next_c) not in visited:
                    queue.append(((next_r, next_c), path + direction))
                    visited.add((next_r, next_c))
    
    return None

def main():
    maze = read_maze('input.txt')
    start, goal = find_start_goal(maze)
    
    if start is None or goal is None:
        print("Error: Start or goal not found in the maze")
        return
    
    path = bfs(maze, start, goal)
    
    if path:
        print(f"S {path} G")
    else:
        print("No path found")

if __name__ == "__main__":
    main() 