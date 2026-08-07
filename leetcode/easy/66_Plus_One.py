# https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=programming-skills

def plusOne(digits: List[int]) -> List[int]:
    new_number = int("".join(map(str,digits))) + 1
    return [int(number) for number in str(new_number)]