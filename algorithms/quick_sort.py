from random import randint


def create_array(size=10, max=100):
    return [randint(0, max) for _ in range(size)]


def quick_sort(a):
    if len(a) <= 1:
        return a
    smaller, equal, larger = [], [], []
    pivot = a[randint(0, len(a) - 1)]

    for x in a:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)

    return quick_sort(smaller) + equal + quick_sort(larger)


if __name__ == "__main__":
    a = create_array(10, 100)
    print(a)
    b = quick_sort(a)
    print(b)
