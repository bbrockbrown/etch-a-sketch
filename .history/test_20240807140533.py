def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    longest = 1
    j = 0
    for i in range(len(s)):
        currString = s[i]
        subs = set(currString)
        j = i + 1
        currLongest = 1
        if j != len(s):
            while j < len(s):
                if s[j] not in subs:
                    currLongest += 1
                    j += 1
            if currLongest > longest:
                longest = currLongest
        else:
            break
    return longest


print(lengthOfLongestSubstring("abcabcbb"))