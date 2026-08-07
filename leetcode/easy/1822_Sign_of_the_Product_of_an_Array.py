# https://leetcode.com/problems/sign-of-the-product-of-an-array/description/?envType=study-plan-v2&envId=programming-skills

import operator
from functools import reduce

def arraySign(nums: list[int]) -> int:
    calculation = reduce(operator.mul, nums)
    
    if calculation > 0: return 1
    elif calculation == 0: return 0
    else: return -1