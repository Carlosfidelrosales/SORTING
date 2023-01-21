def partition(numbers, low, high):
    i = low
    pivot = numbers[high]

    for j in range(low, high):
        if numbers[j] <= pivot:
            numbers[i], numbers[j] =  numbers[j], numbers[i]
            i += 1

    numbers[i], numbers[high] = numbers[high] ,numbers[i]

    return i
