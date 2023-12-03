from collections import defaultdict 

D = open(0).read()

S = ["*"]

def part2():
  lines = D.splitlines(True)

  part_numbers_dict = defaultdict(list)

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
        adj_to = ()

        if (check_start > 0 and line[check_start] in S):
          is_adj = True
          adj_to = (check_start, index)
        elif(check_end < len(line) - 1 and line[check_end] in S):
          is_adj = True
          adj_to = (check_end, index)

        # check above and below
        for i in range(check_start, check_end + 1):
          above = index > 0 and lines[index -1][i] in S
          below = index < len(line) - 1 and lines[index + 1][i] in S
          if above:
            is_adj = True
            adj_to = (i, index-1)
            break
          if below:
            is_adj = True
            adj_to = (i, index+1)
            break

        if is_adj:
          part_numbers_dict[adj_to].append(full_number)

        number_start = -1
        number_end = -1

  sum = 0
  for k in part_numbers_dict:
    if len(part_numbers_dict[k]) == 2:
      ratio = 1
      for el in part_numbers_dict[k]:
        ratio *= el
      
      sum += ratio
  
  print("p2",sum)

if __name__ == '__main__':
  part2()