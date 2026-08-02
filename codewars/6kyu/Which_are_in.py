def in_array(array1: list[str], array2: list[str]):
    answer: set = set()

    for check in array1:
        for word in array2:
            if check in word:
                answer.add(check)
                break

    return sorted(answer)


print(
    in_array(
        array1=["arp", "live", "strong"],
        array2=["lively", "alive", "harp", "sharp", "armstrong"],
    )
)
