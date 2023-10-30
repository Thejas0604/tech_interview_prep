class Solution:
    def isValid(self, s: str) -> bool:
        dict = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for i in s:
            if i in dict:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                elif dict[stack.pop()] != i:
                    return False
        return True if len(stack) == 0 else False

solution = Solution()
print(solution.isValid("()"))

