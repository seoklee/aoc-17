def parse_input(file):
    file = open("input.txt", "r'")
    return list(map(int, file.read().rstrip()))


def part_one(input):
    result = 0
    for index, num in enumerate(input):
        if num == input[(index+1) % len(input)]:
            result += num

    return result


def part_two(input):
    result = 0

    for index, num in enumerate(input):
        if num == input[(len(input) / 2) + (int(index))]:
            result = result + (int(num) * 2)

        if index == (len(input)/2) - 1:
            break

    return result

print part_one(parse_input(file))
print part_two(parse_input(file))

