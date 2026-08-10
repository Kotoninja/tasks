# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python


def delete_nth(order, max_e):
    hash_map: dict = {}

    i = 0
    while i < len(order):
        number = order[i]
        hash_map[number] = hash_map.get(number, 0) + 1

        if hash_map[number] > max_e:
            order = order[:i] + order[i + 1 :]
        else:
            # next iter
            i += 1
    return order


print(delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 2))
