from collections import deque

def find_path(maze):
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    rows, cols = len(maze), len(maze[0])
    start, goal = None, None
    
    # Locate start (S) and goal (G) positions
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'G':
                goal = (r, c) 
     
    # BFS initialization
    queue = deque([(start, '')])
    visited = set([start])
    
    while queue:
        (x, y), path = queue.popleft()
        
        if (x, y) == goal:
            return path + 'G'
        
        for direction, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + direction))
    
    return "NO PATH"

def main():
    # Read input from input.txt
    with open('./input.txt', 'r') as file:
        maze = [list(line.strip()) for line in file.readlines()]
    
    # Find and print the path
    result = find_path(maze)
    print(result)

if __name__ == "__main__":
    main()
