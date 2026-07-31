def numRescueBoats(people: list[int], limit: int) -> int:
    answer = 0

    l, r = 0, len(people) - 1
    people.sort()
    while l <= r:
        if people[l] + people[r] <= limit:
            answer += 1
            l += 1
            r -= 1

        elif people[r] <= limit:
            answer += 1
            r -= 1
    return answer


print(numRescueBoats(people=[1, 2], limit=3))
print(numRescueBoats(people=[3, 2, 2, 1], limit=3))
print(numRescueBoats(people=[3, 5, 3, 4], limit=5))
print(numRescueBoats(people=[3, 3, 4], limit=7))
print(numRescueBoats(people=[3, 3, 3, 4], limit=7))
