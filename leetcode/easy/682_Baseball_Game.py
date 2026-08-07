# https://leetcode.com/problems/baseball-game/description/?envType=study-plan-v2&envId=programming-skills


def calPoints(operations: list[str]) -> int:
    record = []
    
    
    for value in operations:
        if value == "+":
            record.append(sum(record[-2:]))
        elif value == "D":
            record.append(record[-1]*2)
        elif value == "C":
            record.pop()
        else:
            record.append(int(value))
    return sum(record)


print(calPoints(["5","2","C","D","+"]))
print(calPoints(["5","-2","4","C","D","9","+","+"]))
print(calPoints(["1","C"]))