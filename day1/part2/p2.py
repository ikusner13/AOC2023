value_dict = {
    'one': "1",
    'two': "2",
    'three': "3",
    'four': "4",
    'five': "5",
    'six': "6",
    'seven': "7",
    'eight': "8",
    'nine': "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
}

with open('input.txt', 'r') as f:
  sum = 0
  for line in f:
    line.strip()

    search_terms = list(value_dict.keys())
    
    firstDigit = ""
    lastDigit = ""
    firstDigitIndex = len(line)
    lastDigitIndex = -1

    for term in search_terms:
        if term in line:
            firstIndex = line.index(term)
            lastIndex = line.rindex(term)

            if firstIndex < firstDigitIndex:
                firstDigitIndex = firstIndex
                firstDigit = value_dict[term]
            
            if lastIndex > lastDigitIndex:
                lastDigitIndex = lastIndex
                lastDigit = value_dict[term]

    sum += int(firstDigit + lastDigit)

  print(sum)