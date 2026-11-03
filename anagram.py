def is_anagram(word1,word2):
    return sorted(word1)==sorted(word2)

word1="heart"
word2="earth"
result=is_anagram(word1,word2)
print(result)
