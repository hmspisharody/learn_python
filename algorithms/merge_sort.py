
def create_array(size=10, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]


def merge(a, b):
    a_i = 0
    b_i = 0
    c = []
    while a_i < len(a) and b_i < len(b):
        if a[a_i] <= b[b_i]:
            c.append(a[a_i])
            a_i += 1
        elif b[b_i] <= a[a_i]:
            c.append(b[b_i])
            b_i += 1
    if a_i == len(a):
        c.extend(b[b_i:])
    else:
        c.extend(a[a_i:])
    return c

def merge_sort(a):
    if len(a) == 1:
        return a

    l, r = merge_sort(a[:len(a) // 2]), merge_sort(a[len(a) // 2:])

    return merge(l, r)


if __name__ == "__main__":
    a = create_array(10, 100)
    print(a)
    b = merge_sort(a)
    print(b)
