def removeDuplicates(nums: list[int | str]) -> int:
    index = 0
    for _ in range(len(nums)):
        if index == len(nums)-1:
            index+=1
            break
        elif nums[index + 1] == nums[index]:
            del nums[index]
        else:
            index += 1
    return index


# print(removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates(nums = [1,2]))