

def wordBreak(s, wordDict):
    """if s == "":
        return True
    for word in wordDict:
        if len(word) > len(s):
            continue
        if word == s[:len(word)]:
            return wordBreak("""
    solution = [False] * len(s)
    for i in range(len(s)):
        for word in wordDict:
            if word == s[i - len(word) + 1 : i + 1] and (solution[i - len(word)] or i - len(word) < 0): # if the word ends at ith index of s and there already existed a word that ended at the beginning of that word
                solution[i] = True
    return solution[-1]

print(wordBreak("leetcode", ["leet","code"]))
print(wordBreak("applepenapple",["apple","pen"]))
print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))

