with open('input.txt', 'r') as f:
    sum = 0
    for line in f:
        line.strip()

        firstIndex = 0
        lastIndex = len(line) - 1

        firstChar = line[0]
        lastChar = line[-1]

        while not (firstChar.isdigit() and lastChar.isdigit()):
            if not firstChar.isdigit():
                firstChar = line[firstIndex + 1]
                firstIndex += 1
            if not lastChar.isdigit():
                lastChar = line[lastIndex - 1]
                lastIndex -= 1
            
            if firstIndex == lastIndex:
                break
        
        sum += int(firstChar + lastChar)
        
    print(sum)
