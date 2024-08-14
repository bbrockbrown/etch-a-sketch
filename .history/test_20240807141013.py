def lengthOfLongestSubstring(s):
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
                currString = s[j]
                if currString not in subs:
                    currLongest += 1
                    j += 1
                    subs.add(currString)
                else:
                    break
            if currLongest > longest:
                longest = currLongest
        else:
            break
    return longest


print(lengthOfLongestSubstring("pwwkew"))