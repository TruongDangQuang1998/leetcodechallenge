from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        len_digits = len(digits)
        
        while len_digits > 0:
            if digits[len_digits -1] + 1 == 10:
                if len_digits - 2 >= 0:
                    if digits[len_digits - 2] + 1 == 10:
                        if len_digits - 2 == 0:
                            digits[len_digits - 1] = 0
                            digits[len_digits - 2] = 1
                            digits.append(0)
                            break
                        else:
                            digits[len_digits - 1] = 0
                    else:
                        digits[len_digits - 1]= 0
                        digits[len_digits - 2]= digits[len_digits - 2] + 1
                        break
                    len_digits-= 1
                else:
                    digits[len_digits -1] = 1
                    digits.append(0)
                    break
            else:
                digits[len_digits -1]  = digits[len_digits -1] + 1
                break

        for x in digits:
            if result:
                result.append(x)
            elif x != 0:
                result.append(x)
        return result
solution  = Solution()
result = solution.plusOne([8,9,9,9])
print(result)
result = solution.plusOne([9])
print(result)
result = solution.plusOne([9,9])
print(result)
