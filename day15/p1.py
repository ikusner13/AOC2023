D = open(0).read()

"""
Determine the ASCII code for the current character of the string.
Increase the current value by the ASCII code you just determined.
Set the current value to itself multiplied by 17.
Set the current value to the remainder of dividing itself by 256.
"""


def hash_algo(input_str):
    current_value = 0

    for char in input_str:
        current_value = (current_value + ord(char)) * 17 % 256

    return current_value


def part1():
    strings = D.split(",")

    print(sum(hash_algo(i) for i in strings))


if __name__ == "__main__":
    part1()
