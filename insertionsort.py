def insertion_sort(numbers):  
    for i in range(1, len(numbers)):  
        current = numbers[i]  

        j = i - 1  
        while j >= 0 and current < numbers[j]:  
            numbers[j+1] = numbers[j]  
            j -= 1  
        numbers[j+1] = current  

    return numbers


def main():
    numbers = [75, 43, 69, 73, 52, 86, 91, 49, 57, 1]
    insertion_sort(numbers)
    print(numbers)

main()