# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c
def max_sequence(arr):
    if not arr:
        return 0
    max_numbers = arr[0]

    inter_numbers = arr[0]

    negative_numbers_count = 0
    
    for i in range(1, len(arr)):
        number = arr[i]
        if number<0:
            negative_numbers_count +=1
        inter_numbers = max(inter_numbers + number, number)
        max_numbers = max(inter_numbers, max_numbers)

    return max_numbers if negative_numbers_count != len(arr)-1 else 0

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
