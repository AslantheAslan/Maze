import maze

def main():

    m = maze.MazeSolver('file.txt')
    m.solve_maze()

    try:
        map = maze.text_to_array('file.txt')
        validation = maze.Maze(map)
        print("where", validation.get_start(), "is start and", validation.get_end(), "is the end cell")
    except maze.InvalidMazeException as e:
        print(e)

if __name__ == '__main__':
    main()