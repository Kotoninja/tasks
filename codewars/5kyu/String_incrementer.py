# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python


def increment_string(string: str):
    if not string:
        return "1"
    elif not string[-1].isdigit():
        return string + "1"
    
    r = len(string) -1
    while string[r].isdigit() and r>0:
        r-=1
    
    if r == len(string)-1:
        return str(int(string)+1).zfill(r)
    return string[:r+1] + str(int(string[r+1:])+1).zfill(len(string)-1-r)


print(increment_string("foo1"))
print(increment_string("foosdfasdf0001"))
print(increment_string("1"))
print(increment_string("009"))
