import numpy as np
import time
from functools import wraps

nums = list(np.random.randint(low=1, high=20, size=2000))


def time_sorts(fn):
    @wraps(fn)
    def time_calc(*args, **kwargs):
        t_start = time.time()
        sorted_list = fn(*args, **kwargs)
        t_end = time.time()
        return [sorted_list, t_end - t_start]


def binary_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


# print(f"Original array : {nums}")
start_time = time.time()

# bubble sort
for i in range(len(nums)):
    for j in range(len(nums) - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
end_time = time.time()
print(f'bubble sort Time : {end_time - start_time} seconds')

# time built-in sort method
nums = np.random.randint(low=1, high=20, size=2000)
start_time = time.time()
nums1 = np.sort(nums)
end_time = time.time()
print(f'nums.sort() Time : {end_time - start_time} seconds')
