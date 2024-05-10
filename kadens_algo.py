"""
Find the Sum of the longest contiguous subarray
----------------------------------------------------------
Kaden's Algo:
  1. Iterate over array
  2. Sum from index 1 to forward and compared with the max sum
  3. Once Sum will be less than 0, sum will be default to 0
"""


def sub_arr_sum(arr):
    sum = 0
    max_sum = 0
    
    for x in arr:
        sum += x
        max_sum = max(sum, max_sum)
        sum = 0 if sum < 0 else sum
    
    return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(sub_arr_sum(arr))
