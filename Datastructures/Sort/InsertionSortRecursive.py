def InsertionSortRecursive(A, n):
    if n <= 1:
        return

    InsertionSortRecursive(A, n - 1)
    key = A[n - 1]
    j = n - 2

    while j >= 0 and A[j] > key:
        A[j + 1] = A[j]
        j = j - 1

    A[j + 1] = key


def InsertionSort(A):
    InsertionSortRecursive(A, len(A))


