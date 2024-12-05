def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

if __name__ == "__main__":
    numbers = []
    try:
        n = int(input("Enter the number of elements: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            for i in range(n):
                while True:
                    try:
                        num = float(input(f"Enter element {i+1}: "))
                        numbers.append(num)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

            sorted_numbers = bubble_sort(numbers)
            print("Sorted numbers:", sorted_numbers)
    except ValueError:
        print("Invalid input for the number of elements. Please enter an integer.")