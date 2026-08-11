# https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75


def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    if len(flowerbed) == 1:
        if not flowerbed[0]:
            if n <= 1:
                return True
            else:
                return False
        elif flowerbed[0]:
            if n == 0:
                return True
            else:
                return False

    for i in range(len(flowerbed)):
        if i == 0:
            if not flowerbed[i] and not flowerbed[i + 1]:
                n -= 1
                flowerbed[i] = 1
        elif i == len(flowerbed) - 1:
            if not flowerbed[i] and not flowerbed[i - 1]:
                n -= 1
                flowerbed[i] = 1
        else:
            if not flowerbed[i] and (not flowerbed[i + 1] and not flowerbed[i - 1]):
                n -= 1
                flowerbed[i] = 1

    return n <= 0


print(canPlaceFlowers(flowerbed=[0], n=1))
print(canPlaceFlowers(flowerbed=[1], n=1))
print(canPlaceFlowers(flowerbed=[1], n=0))
print(canPlaceFlowers(flowerbed=[0], n=0))
print(canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))
print(canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))
print(canPlaceFlowers(flowerbed=[1, 0, 0, 0, 0, 1], n=2))
