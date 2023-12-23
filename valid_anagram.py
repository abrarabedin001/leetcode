class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        first_dict = {}
        second_dict = {}

        for letter in s:
            first_dict[letter] = first_dict.get(letter, 0) + 1
        for letter in t:
            second_dict[letter] = second_dict.get(letter, 0) + 1
        
        for letter in s:
            if second_dict.get(letter, 0) != first_dict.get(letter, 0):
                return False
        
        return True