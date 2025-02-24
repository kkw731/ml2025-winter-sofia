class NumberStorage:
    def __init__(self):
        self.numbers = []

    def add_number(self, num):
        """ Adds a number to the list """
        self.numbers.append(num)

    def find_number(self, x):
        """ Returns 1-based index if found, else -1 """
        try:
            return self.numbers.index(x) + 1  # Convert 0-based index to 1-based
        except ValueError:
            return -1