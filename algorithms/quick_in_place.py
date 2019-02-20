from random import randint


def create_array(size=10, max=100):
    return [randint(0, max) for _ in range(size)]


def partition(a, low, high):
    i = low - 1

    for j in range(low, high):
        if a[j] < a[high]:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def quicksort_inplace(a, low=0, high=None):
    if high == None:
        high = len(a) - 1
    if low < high:
        pos = partition(a, low, high)
        quicksort_inplace(a, low, pos - 1)
        quicksort_inplace(a, pos + 1, high)


a = create_array()
print(a)
quicksort_inplace(a)
print(a)
