class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1 
        word = 0
        while i >= 0:
            if s[i] == ' ':
                if word != 0:
                    break
            else: word += 1
            i-=1
        return word
solution= Solution()
str= "Hello World"
result = solution.lengthOfLastWord(str)
print(result)
