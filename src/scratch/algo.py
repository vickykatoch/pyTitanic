import numpy as np
import math
# 4,4,6,7,9,10,11,12,14,15
# IQTILE=6 :, Median : 9.5, Mean: , Mode
# 4,4,6,7,9,10,11,12,14,15,16
# IQTILE=8 :, Median : 10, Mean: , Mode
numbers = np.array([4,4,10,11,15,7,14,12,6,9])

def calc_iqtile(nums):
    sorted_nums = np.sort(nums)
    size = nums.size
    print('Sorted : {}'.format(sorted_nums))
    if size % 2 == 0:
        left, right = np.split(sorted_nums,2)
        mi = math.floor(left.size/2)
        return right[mi] - left[mi]
    else:
        midx = math.floor(sorted_nums.size/2)
        left, middle, right = np.split(sorted_nums,[midx,midx+1])
        return right[math.floor(right.size/2)] - left[math.floor(left.size/2)]

value = calc_iqtile(numbers)
print(value);
