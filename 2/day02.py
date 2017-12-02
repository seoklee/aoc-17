from solution import Solution


class SolutionDayTwo(Solution):
    def parse_input(self, test_input=None):
        if test_input is None:
            list = []
            for line in self.file:
                line = line.rstrip()
                row = [int(x) for x in line.split("\t")]
                list.append(row)
            return list

    def solve_part_one(self, test_input=None):
        result = 0

        for row in self.solution_input:
            row.sort()
            result = result + row[len(row) - 1] - row[0]

        print result

    def solve_part_two(self, test_input=None):
        result = 0
        for row in self.solution_input:
            row.sort(reverse=True)
            for num in row:
                found = False
                last_index = len(row) - 1
                while found is False:
                    # found
                    if num % row[last_index] == 0:
                        found = True
                    # not found
                    else:
                        last_index = last_index - 1

                if row[last_index] == num:
                    continue
                else:
                    result = result + num / row[last_index]
                    break
        print result

if __name__ == "__main__":
    day_one = SolutionDayTwo()
    day_one.solve_part_one()
    day_one.solve_part_two()
