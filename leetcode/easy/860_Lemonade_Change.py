# https://leetcode.com/problems/lemonade-change/description/?envType=study-plan-v2&envId=programming-skills


def lemonadeChange(bills: list[int]) -> bool:
    money_map = {5: 0, 10: 0, 20: 0}

    for bill in bills:
        change = bill - 5 

        if change == 5:
            if money_map[5] > 0:
                money_map[5] -= 1
            else:
                return False

        elif change == 15:
            if money_map[10] > 0 and money_map[5] > 0:
                money_map[10] -= 1
                money_map[5] -= 1
            elif money_map[5] >= 3:
                money_map[5] -= 3
            else:
                return False

        if bill == 5:
            money_map[5] += 1
        elif bill == 10:
            money_map[10] += 1
        elif bill == 20:
            money_map[20] += 1

    return True


# print(lemonadeChange(bills=[5, 5, 5, 10, 20]))
# print(lemonadeChange(bills=[5, 5, 10, 10, 20]))
print(lemonadeChange(bills=[5, 5, 5, 10, 5, 5, 10, 20, 20, 20]))
