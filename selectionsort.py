def selection_sort(numbers):
    num = len(numbers)

    for i in range(num-1): 
        min = i

        for j in range(i+1, num):
            if numbers[j] < numbers[min]:
                min = j

        if min != i:
            temp = numbers[i]
            numbers[i] = numbers[min]
            numbers[min] = temp

    return numbers


def main():
    numbers = [75, 43, 69, 73, 52, 86, 91, 49, 57, 1]
    selection_sort(numbers)
    print(numbers)

main()