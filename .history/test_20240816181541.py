def groupAnagrams(strs):
    out = []
    mapping = {}
    i = 0
    for word in strs:
        found = False
        if mapping:
            for key in mapping:
                if set(word) == set(mapping[key][0]) and len(word) == len(mapping[key][0]):
                    mapping[key].append(word)
                    found = True
            if not found:
                mapping[str(i)] = word
                i += 1
        else:
            mapping[i] = word
            i += 1

    for ky in mapping:
        for char in mapping[ky]:
            print(char)
            out.append(char)
        print()
        
    
    return out


print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))