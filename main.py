def get_int_range(prompt, low, high):
  val = 0
  valid = False
  while not valid:
    try:
      val = int(input(prompt))
      if val >= low and val <= high:
        valid = True
      else:
        print("Invalid input - should be within range " + str(low) + "-" + str(high) + ".")
    except ValueError:
      print("Invalid input - should be an integer.")
  return val

def read_maze():

    file = open('maze.txt')
    list2d = []
    for row in file:
        list = []
        for item in row:
            if item != '\n':
                list.append(item)
        list2d.append(list)
    return list2d

def find_start(maze):

    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if maze[x][y] == 's':
                return [x,y]

def display_maze(maze, loc):

    for x, row in enumerate(maze):
        for y, char in enumerate(row):
            if [x, y] == loc:
                print("X", end=" ")
            else:
                print(char, end=" ")
        print()

def main():

    print('-Maze Solver-')
    maze = read_maze()
    user_loc = find_start(maze)

    while True:

        display_maze(maze, user_loc)
        print("1. Go North \n2. Go South \n3. Go East \n4. Go West")

        user_input = get_int_range("Enter a Choice: ",1,4)

        if user_input == 1:
            new_loc = [user_loc[0] - 1 , user_loc[1]]
        if user_input == 2:
            new_loc = [user_loc[0] + 1 , user_loc[1]]
        if user_input == 3:
            new_loc =  [user_loc[0] , user_loc[1] + 1]
        if user_input == 4:
            new_loc = [user_loc[0] , user_loc[1] - 1]
        if maze[new_loc[0]][new_loc[1]] == '*':
            print("You can not go that way!")
        else:
            user_loc = new_loc
            if maze[new_loc[0]][new_loc[1]] == 'f':
                display_maze(maze,user_loc)
                print("CONGRATULATIONS! You solved the maze")
                break
main()