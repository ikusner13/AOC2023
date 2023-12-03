D = open(0).read()

S = ["*", '+', '$', "#", "/", "@", "%", '=', "&", "-"]

def check_adjacent(start, end, line, lines, index):
  # check next to
  if (start > 0 and line[start] in S) or (end < len(line) - 1 and line[end] in S):
    return True

  # check above and below
  for i in range(start, end + 1):
    above = index > 0 and lines[index -1][i] in S
    below = index < len(line) - 1 and lines[index + 1][i] in S
    if above or below:
      return True



def part1():
  lines = D.splitlines()

  part_numbers = []

  for index, line in enumerate(lines):
    number_start = -1
    number_end = -1
    for line_index, char in enumerate(line):
      if char.isdigit() and number_start == -1:
        number_start = line_index
        number_end = line_index
      elif char.isdigit() and number_start != -1:
        number_end = line_index

      if number_start == -1 and number_end == -1:
        continue

      if char == "." or line_index == len(line) - 1 or char in S:
        full_number = int(line[number_start:number_end+1])

        check_start = max(number_start - 1, 0)
        check_end = min(number_end + 1, len(line) - 1)
        
        is_adj = False

        if (check_start > 0 and line[check_start] in S):
          is_adj = True
        elif(check_end < len(line) - 1 and line[check_end] in S):
          is_adj = True

        # check above and below
        for i in range(check_start, check_end + 1):
          above = index > 0 and lines[index -1][i] in S
          below = index < len(line) - 1 and lines[index + 1][i] in S
          if above:
            is_adj = True
            break
          if below:
            is_adj = True
            break

        if is_adj:
          part_numbers.append(full_number)

        number_start = -1
        number_end = -1

  print("p1", sum(part_numbers))

if __name__ == '__main__':
  part1()