def to_camel_case(text: str) -> str:
    index = 1
    n = len(text)
    is_word = False
    while index <= n - 1:
        if text[index] in "-_":
            text = text[:index] + text[index + 1 :]
            n -= 1
            is_word = True
            continue
        if is_word:
            text = text[:index] + text[index].upper() + text[index + 1 :]
            is_word = False
        index += 1
    return text


print(to_camel_case(""))
print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))
print(to_camel_case("A-B-C"))
