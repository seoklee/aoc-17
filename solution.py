class Solution(object):
    # file = open("input.txt", "r'")
    input = None

    def __init__(self):
        self.file = self.open_file()
        self.solution_input = self.parse_input()

    def open_file(self):
        return open("input.txt", "r'")

    def parse_input(self): pass

    def solve_part_one(self, test_input=None): pass

    def solve_part_two(self, test_input=None): pass
