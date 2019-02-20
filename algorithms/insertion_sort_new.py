import time

def create_array(size=10, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]


def insertion_sort(a):
    for sel_item in range(1, len(a)):
        cur_item = a[sel_item]
        cur_idx = sel_item
        prev_item = a[cur_idx-1]
        while cur_idx > 0 and cur_item < prev_item:
            a[cur_idx] = prev_item
            cur_idx -= 1
            prev_item = a[cur_idx-1]
        a[cur_idx] = cur_item
    return a


if __name__ == "__main__":
    nums = create_array(10000, 500)
    st_time = time.time()
    nums_sorted = insertion_sort(nums)
    end_time = time.time()
    diff_time = end_time - st_time
    
    print('Time Taken : ' + str(diff_time * 1000) + ' msecs')
