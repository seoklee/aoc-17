class SolutionDayFour(Solution):
    def parse_input(self):
        list = []
        for line in self.file:
            line = line.rstrip()
            row = [x for x in line.split(" ")]
            list.append(row)
        return list

    def solve_part_one(self, test_input=None):
        result = 0
        for row in self.solution_input:
            x = set(row)
            if len(row) == len(x):
                result = result + 1
        print result

    def solve_part_two(self, test_input=None):
        result = 0
        for row in self.solution_input:
            word_set = set()
            for word in row:
                sorted_word = ''.join(sorted(word))
                word_set.add(sorted_word)

            if len(word_set) == len(row):
                result = result + 1

        print result


if __name__ == "__main__":
    day_four = SolutionDayFour()
    day_four.solve_part_one()
    day_four.solve_part_two()