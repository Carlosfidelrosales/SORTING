def insertion_sort(numbers):  
    for i in range(1, len(numbers)):  
        current = numbers[i]  

        j = i - 1  
        while j >= 0 and current < numbers[j]:  
            numbers[j+1] = numbers[j]  
            j -= 1  
        numbers[j+1] = current  

    return numbers

