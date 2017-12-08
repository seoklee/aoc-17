def parse_input():
    file = open("input.txt", "r'")
    return [line.rstrip().split(" ") for line in file]


def part_one(input):
    result = 0
    for row in input:
        result += 1 if len(set(row)) == len(row) else 0
    return result


def part_two(input):
    result = 0
    for row in input:
        word_set = set([''.join(sorted(word)) for word in row])
        result += 1 if len(set(word_set)) == len(row) else 0

    return result


print part_one(parse_input())
print part_two(parse_input())