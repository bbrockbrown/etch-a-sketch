def isPalindrome(s: str) -> bool:
        s = "".join([x for x in s if x.isalpha()])
        print(s)
        print(s[::-1])
        return s == s[::-1]
            
            
print(isPalindrome("Was it a car or a cat I saw?"))