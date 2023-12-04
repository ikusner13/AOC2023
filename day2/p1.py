data = open(0).read()

possible_red = 12
possible_green = 13
possible_blue = 14

def is_set_possible(set):
  cubes = set.split(",")

  for cube in cubes:
    split_cube = cube.split(" ")
    cube_color = split_cube[2]
    cube_number = int(split_cube[1])

    if cube_color == "red" and cube_number > possible_red:
      return False
    elif cube_color == "green" and cube_number > possible_green:
      return False
    elif cube_color == "blue" and cube_number > possible_blue:
      return False
    
  return True

def is_game_possible(game):
  for set in game:
    valid = is_set_possible(set)
      
    if not valid:
      return False
  
  return True


def part1():
  possible_games = []
  for index, line in enumerate(data.splitlines(), start=1):
    line = line.split(':')
    set_section = line[1].split(";")
    
    if is_game_possible(set_section):
      possible_games.append(int(index))

  print(sum(possible_games))

    
if __name__ == '__main__':
  part1()