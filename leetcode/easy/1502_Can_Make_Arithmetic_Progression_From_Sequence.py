# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/?envType=study-plan-v2&envId=programming-skills


def canMakeArithmeticProgression(arr: list[int]) -> bool:
    arr.sort()
    difference = abs(arr[1] - arr[0])

    for i in range(0, len(arr) - 1):
        if abs(arr[i + 1] - arr[i]) != difference:
            return False

    return True


print(
    canMakeArithmeticProgression(
        [
            -509,
            -19,
            -439,
            -264,
            -404,
            -369,
            -299,
            -89,
            -229,
            -54,
            -194,
            16,
            -544,
            -159,
            -124,
            -474,
            -334,
        ]
    )
)
