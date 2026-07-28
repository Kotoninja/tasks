def isPalindrome(s: str) -> bool:
    main_string = "".join([i for i in s.lower() if i.isalnum()])

    if not main_string:
        return True

    left, right = 0, len(main_string) - 1

    
    while left <= right:
        if main_string[left] != main_string[right]:
            return False

        left, right = left + 1, right - 1
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome(s="race a car"))
print(isPalindrome(s=" "))
print(isPalindrome(s="aa"))
