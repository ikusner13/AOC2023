import re

replacement_dict = {
  "one": "o1e",
  "two": "t2o",
  "three": "t3e",
  "four": "f4r",
  "five": "f5e",
  "six": "s6x",
  "seven": "s7n",
  "eight": "e8t",
  "nine": "n9e",
}

def replace_line(line): 
    for key, value in replacement_dict.items():
      line = line.replace(key, value)
  
    return line

data = open(0).read()

sum = 0

for line in data.splitlines():
  replaced = replace_line(line)

  digits = re.findall(r'\d', replaced)

  sum += int(digits[0] + digits[-1])

print(sum)
