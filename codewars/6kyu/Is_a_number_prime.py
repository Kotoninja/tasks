def is_prime(num):
    if num <= 1:
        return False

    count_of_division = 1
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            count_of_division+=1

    return count_of_division <= 2


print(is_prime(1))
print(is_prime(2))
print(is_prime(73))
print(is_prime(75))
print(is_prime(3))
print(is_prime(5))
print(is_prime(7))
print(is_prime(9))
