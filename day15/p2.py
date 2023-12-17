from collections import defaultdict

D = open(0).read()


def hash_algo(input_str):
    current_value = 0

    for char in input_str:
        current_value = (current_value + ord(char)) * 17 % 256

    return current_value


def focusing_power_for_box(box, box_number):
    return sum(box_number * (i + 1) * b[1] for i, b in enumerate(box))


def part2():
    labels = D.split(",")
    hashmap = defaultdict(list)

    for label in labels:
        lens_label, *rest = label.split("-" if "-" in label else "=")
        current_box = hashmap[hash_algo(lens_label)]

        if "-" in label:
            current_box[:] = [t for t in current_box if t[0] != lens_label]

        elif "=" in label:
            tup = (lens_label, int(rest[0]))

            for i, t in enumerate(current_box):
                if t[0] == lens_label:
                    current_box[i] = tup
                    break
            else:
                current_box.append(tup)

    total_power = sum(
        focusing_power_for_box(value, key + 1)
        for key, value in hashmap.items()
        if value
    )

    print(total_power)


if __name__ == "__main__":
    part2()
