def groupAnagrams(strs):
    out = []
    mapping = {}
    i = 0
    for word in strs:
        found = False
        if mapping:
            for key in mapping:
                if set(word) in set(mapping[key][0]) and len(word) == len(mapping[key]):
                    mapping[key].append(word)
                    found = True
            if not found:
                mapping[i] = word
                i += 1
        else:
            mapping[i] = word
            i += 1

    for ky in mapping:
        for char in ky:
            out.append(char)
    
    return out


print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))