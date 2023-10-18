import random
import time
import matplotlib.pyplot as plt

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

# Selection Sort
def selection_sort(a):
    n = len(a)
    for start in range(n):
        minpos = start
        for i in range(start + 1, n):
            if a[i] < a[minpos]:
                minpos = i
        swap(a, start, minpos)

# Insertion Sort
def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Generate random data for sorting
array = [45,23,67,12,98,34,56,72,19,81,37,59,64,28,53,90,14,60,88,42]

# Sort arrays using different algorithms
selection_sorted_array = array.copy()
selection_sort(selection_sorted_array)

insertion_sorted_array = array.copy()
insertion_sort(insertion_sorted_array)

merge_sorted_array = merge_sort(array.copy())

# Measure execution time for each sorting algorithm
start_time = time.time()
selection_sort(array.copy())
selection_time = time.time() - start_time

start_time = time.time()
insertion_sort(array.copy())
insertion_time = time.time() - start_time

start_time = time.time()
merge_sort(array.copy())
merge_time = time.time() - start_time

# Plotting the execution time
sorting_algorithms = ['Selection Sort', 'Insertion Sort', 'Merge Sort']
execution_times = [selection_time, insertion_time, merge_time]

plt.bar(sorting_algorithms, execution_times, color=['blue', 'green', 'orange'])
plt.ylabel('Execution Time (s)')
plt.title('Execution Time of Sorting Algorithms')
plt.show()

print("Array sorted using Selection Sort:", selection_sorted_array)
print("Array sorted using Insertion Sort:", insertion_sorted_array)
print("Array sorted using Merge Sort:", merge_sorted_array)




        
