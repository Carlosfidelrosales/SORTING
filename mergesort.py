def merge_sort(numbers):
    length = len(numbers)

    if length == 1:
        return numbers

    mid = length // 2

    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])

    return merge(left, right)


def merge(left, right):
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    output.extend(left[i:])
    output.extend(right[j:])

    return output


def main():
    unsorted = [75, 43, 69, 73, 52, 86, 91, 49, 57, 1]
    sorted = merge_sort(unsorted)
    print(sorted)

main()
