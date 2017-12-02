from solution import Solution


class SolutionDayOne(Solution):
    def parse_input(self, test_input=None):
        if test_input is None:
            return list(self.file.read())
        else:
            return list(test_input)

    def solve_part_one(self, test_input=None):
        result = 0
        for index, num in enumerate(self.solution_input):
            if index != len(self.solution_input)-1 and num == self.solution_input[index+1]:
                result = result + int(num)
            if index == len(self.solution_input)-1 and num == self.solution_input[0]:
                result = result + int(num)
        print result

    def solve_part_two(self, test_input=None):
        result = 0
        for index, num in enumerate(self.solution_input):
            if num == self.solution_input[(len(self.solution_input) / 2) + (int(index))]:
                result = result + (int(num) * 2)

            if index == (len(self.solution_input)/2)-1:
                break
        print result


if __name__ == "__main__":
    day_one = SolutionDayOne()
    day_one.solve_part_one()
    day_one.solve_part_two()
