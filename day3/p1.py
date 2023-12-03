D = open(0).read()

S = ["*", '+', '$', "#", "/", "@", "%", '=', "&", "-"]

def part1():
  lines = D.splitlines(True)

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

      if char == "." or line_index == len(line) - 1 or char in S:
        if number_start != -1 and number_end != -1:
          full_number = line[number_start:number_end+1]

          is_adj_to_symbol = False

          # check above
          if index > 0:
            for i in range(int(number_start), int(number_end) + 1):
              adj = lines[index -1][i]
              if adj in S:
                is_adj_to_symbol = True
                break
          # check below
          if index < len(line) - 1:
            for i in range(int(number_start), int(number_end) + 1):
              adj = lines[index +1][i]
              if adj in S:
                is_adj_to_symbol = True
                break
          # check next to
          if number_start > 0 and line[int(number_start - 1)] in S:
            is_adj_to_symbol = True
          if number_end < len(line) - 1 and line[int(number_end + 1)] in S:
            is_adj_to_symbol = True
          
          # check adjacent to
          if number_start > 0:
            if lines[index - 1][number_start - 1] in S:
              is_adj_to_symbol = True
            if index < len(line) - 1:
              if lines[index + 1][number_start - 1] in S:
                is_adj_to_symbol = True
          
          if number_end < len(line) - 1:
            if lines[index - 1][number_end + 1] in S:
              is_adj_to_symbol = True
            if index < len(line) - 1:
              if lines[index + 1][number_end + 1] in S:
                is_adj_to_symbol = True
          
          if is_adj_to_symbol:
            part_numbers.append(int(full_number))
          
          number_start = -1
          number_end = -1

  print("p1", sum(part_numbers))

if __name__ == '__main__':
  part1()