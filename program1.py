from typing import List

def smallest_missing_positive_integer(nums: List[int]) -> int:
    nums_set = set(nums)
    smallest_positive = 1

    while smallest_positive in nums_set:
        smallest_positive += 1

    return smallest_positive


    



  

