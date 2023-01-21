def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n-1):
        for j in range(n-1):
            if numbers[j] > numbers[j+1]: 
                tmp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = tmp

    return numbers

