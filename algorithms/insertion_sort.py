

def create_array(size=10, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]


def insertion_sort(a):
    for sel_item in range(1, len(a)):
        cur_item = a[sel_item]
        cur_idx = sel_item
        while cur_idx > 0 and cur_item < a[cur_idx - 1]:
            a[cur_idx] = a[cur_idx - 1]
            cur_idx -= 1
        a[cur_idx] = cur_item
    return a


if __name__ == "__main__":
    test_array = create_array(10, 100)
    print(f"test_array = {test_array}")

    print(f"Sorted Array = {insertion_sort(test_array)}")
