class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setList = set()
        for items in nums:
            setList.add(items)
        if(len(setList)==len(nums)):
            return False
        else:
            return True
# i used a set and added the elements in the list
# set can not have duplicates
# then checked the length of the set and the array
# if they are the same then return false except return true

# Time Complexity:

#     Creating an empty set: This operation takes O(1) time complexity as it doesn't depend on the size of the input list.
#     Looping through the nums list and adding each element to the set: In the worst case, this operation takes O(n) time complexity, where 'n' is the number of elements in the input list.
#     Comparing the lengths of the set and the original list: This operation takes O(1) time complexity as it's just comparing two lengths.

# Therefore, the overall time complexity of this code is O(n), where 'n' is the number of elements in the nums list.

# Space Complexity:

#     Creating a set to store unique elements: The space required for the set is directly proportional to the number of unique elements in the input list. In the worst case, if all elements are unique, the set will contain all 'n' elements. So, the space complexity is O(n).

# In summary, the time complexity is O(n), and the space complexity is O(n) for the given code.