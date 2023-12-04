data = open(0).read()

def part2():
  sum = 0
  for line in data.splitlines():
    line = line.split(':')
    set_section = line[1].split(";")

    max_red = 0
    max_green = 0
    max_blue = 0

    for set in set_section:
      cubes = set.split(",")
      for cube in cubes:
        split_cube = cube.split(" ")
        cube_color = split_cube[2]
        cube_number = int(split_cube[1])

        if cube_color == "red" and cube_number > max_red:
          max_red = cube_number
        elif cube_color == "green" and cube_number > max_green:
          max_green = cube_number
        elif cube_color == "blue" and cube_number > max_blue:
          max_blue = cube_number


    power = max_red * max_green * max_blue
    sum += power
  
  print(sum)

if __name__ == '__main__':
  part2()