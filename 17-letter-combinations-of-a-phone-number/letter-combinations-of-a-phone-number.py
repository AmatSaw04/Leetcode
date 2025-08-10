class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        a = []
        b = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        def backtrack(combination, next_digits):
            if not next_digits:
                a.append(combination)
                return
            for letter in b[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])
        
        backtrack("", digits)
        return a