from maze_solver import read_maze, solve_maze, print_solution

def main():
    mazes = read_maze('input.txt')
    for idx, maze in enumerate(mazes):
        label = chr(ord('A') + idx)
        solution = solve_maze(maze)
        print_solution(label, solution)

if __name__ == "__main__":
    main() 