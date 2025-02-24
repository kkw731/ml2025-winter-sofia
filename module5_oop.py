class NumberStorage:
    def __init__(self):
        self.numbers = []

    def add_number(self, num):
        self.numbers.append(num)

    def find_number(self, x):
        return self.numbers.index(x) + 1 if x in self.numbers else -1

def main():
    try:
        # Read N (number of elements)
        N = int(input("Enter the number of elements (N): "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")

        storage = NumberStorage()

        # Read N numbers
        print(f"Enter {N} numbers one by one:")
        for i in range(N):
            num = int(input(f"Number {i+1}: "))
            storage.add_number(num)

        # Read X (search number)
        X = int(input("Enter the number to search (X): "))

        # Search and print result
        result = storage.find_number(X)
        print(result)

    except ValueError as e:
        print(f"Input Error: {e}")

if __name__ == "__main__":
    main()