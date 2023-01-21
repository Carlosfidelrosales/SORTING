def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n-1):
        for j in range(n-1):
            if numbers[j] > numbers[j+1]: 
                tmp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = tmp

    return numbers


def main():
    numbers = [75, 43, 69, 73, 52, 86, 91, 49, 57, 1]
    bubble_sort(numbers)
    print(numbers)

main()