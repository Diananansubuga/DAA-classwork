def swap(A,i,j):
  temp = A[i]
  A[i] = A[j]
  A[j] = temp

def insertionSort(A,n):
  for pos in range(1,n):
    nextpos=pos
    while nextpos>0 and A[nextpos]<A[nextpos-1]:
      swap(A,nextpos,nextpos-1)
      nextpos=nextpos-1

  return A

def verifySorted(A,n):
  for i in range(1,n):
    if A[i] < A[i-1]:
      return False
  return True

# Test the insertion sort function
A = [5, 3, 2, 1, 4]
print("Unsorted list:", A)

# Sort the list using insertion sort
A = insertionSort(A, len(A))

# Verify that the list is sorted
isSorted = verifySorted(A, len(A))

# Print the result
if isSorted:
  print("The list is sorted.")
else:
  print("The list is not sorted.")
