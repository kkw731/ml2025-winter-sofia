def main():
    # Ask the user to input a positive integer N
    N = int(input("Please enter a positive integer N: "))
    
    # Create an empty list to store the N numbers provided by the user
    numbers = []
    
    # Read N numbers one by one
    for i in range(N):
        number = int(input(f"Please enter number {i+1}: "))
        numbers.append(number)
    
    # Ask the user to input an integer X
    X = int(input("Please enter an integer X: "))
    
    # Check if X is in the numbers list
    if X in numbers:
        # Output the index of X (starting from 1)
        print(numbers.index(X) + 1)
    else:
        # If X is not in the list, output -1
        print("-1")

if __name__ == "__main__":
    main()
