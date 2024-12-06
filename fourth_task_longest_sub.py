class Solution:
    def length_of_longest_substr(s: str) -> int:
        chars = [0] * 128
        result = 0
        i = 0
        j = 0
        while j < len(s):
            right_char = s[j]
            chars[right_char] += 1
            while chars[right_char] > 1:
                left_char = s[i]
                chars[left_char] -= 1
                i += 1
            result = max(result, i - j + 1)
        return result