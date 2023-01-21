def partition(numbers, low, high):
    i = low
    pivot = numbers[high]

    for j in range(low, high):
        if numbers[j] <= pivot:
            numbers[i], numbers[j] =  numbers[j], numbers[i]
            i += 1

    numbers[i], numbers[high] = numbers[high] ,numbers[i]

    return i


def quick_sort(numbers, low, high):
    if low < high:
        partition_index = partition(numbers, low, high)
        quick_sort(numbers, low, partition_index - 1)
        quick_sort(numbers, partition_index + 1, high)
