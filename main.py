def bubble_sort(numbers, reverse=False):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (reverse and numbers[j] < numbers[j + 1]) or \
               (not reverse and numbers[j] > numbers[j + 1]):
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
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
                        num = float(input(f"Enter element {i + 1}: "))
                        numbers.append(num)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

            while True:
                direction = input("Sort in ascending order (a) or descending order (d)? ").lower()
                if direction in ('a', 'd'):
                    break
                else:
                    print("Invalid input. Please enter 'a' or 'd'.")

            if direction == 'd':
                reverse = True
            else:
                reverse = False

            sorted_numbers = bubble_sort(numbers, reverse)
            print("Sorted numbers:", sorted_numbers)

    except ValueError:
        print("Invalid input for the number of elements. Please enter an integer.")