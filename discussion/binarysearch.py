# """Binary search algorithm.
def binary_search(array, target):
  """
  Performs a binary search on the given array to find the index of the target element.

  Args:
    array: A sorted array of elements.
    target: The element to search for.

  Returns:
    The index of the target element in the array, or -1 if the target element is not found.
  """

  start = 0
  end = len(array) - 1

  # While the start and end indices are still within the bounds of the array, keep searching.
  while start <= end:
    # Find the middle index of the array.
    mid = (start + end) // 2

    # If the target element is equal to the element at the middle index, return the middle index.
    if array[mid] == target:
      return mid

    # If the target element is less than the element at the middle index, search the left half of the array.
    elif array[mid] > target:
      end = mid - 1

    # If the target element is greater than the element at the middle index, search the right half of the array.
    else:
      start = mid + 1

  # If the target element is not found, return -1.
  return -1

    


    
