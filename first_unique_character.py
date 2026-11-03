def first_unique_character(s):
    frequency = {}

    # Count frequency of each character
    for ch in s:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    # Find first character occurring once
    for i in range(len(s)):
        if frequency[s[i]] == 1:
            return i

    return -1


s = "leetcode"

result = first_unique_character(s)

print(result)
