def selection_sort(a,n):
    n = len(a)
    for s in range(n):
        min_idx = s

        for i in range(s + 1, n):
            if a[i] > a[min_idx]:
                min_idx = i

        # Swap the found minimum element with the first element
        a[s], a[min_idx] = a[min_idx], a[s]

    return a

numbers = [70, 71, 76, 72, 60]
sorted_numbers = selection_sort(numbers)
print("Sorted array in ascending order: ")
print(sorted_numbers)
