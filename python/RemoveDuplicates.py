class Solution:
    import string
    def strStr(self, haystack: str, needle: str) -> int:
        lenneedle =  len(needle)
        lenhaystack = len(haystack)
        for i,l in enumerate(haystack):
            if l == needle[0]:
                oneplus = 1
                while oneplus < lenneedle and  i+oneplus < lenhaystack :
                    if haystack[i+oneplus] != needle[oneplus]: break
                    if oneplus+1 == lenneedle: return i
                    oneplus += 1
                if len(needle) == 1:
                    return i
        return -1
solution = Solution()
a = "sadbutsad"
b = "sad"
result = solution.strStr(a, b)
print(result)