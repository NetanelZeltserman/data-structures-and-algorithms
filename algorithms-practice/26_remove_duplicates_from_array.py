"""
remove the duplicates from a sorted list, using 2 indexes.
do it within the array in a O(n) complexity

iterate over the values, store the last unique value in the left pointer (lp)
increment the right pointer, until a new unique value is found, then,
set the left pointer to the unique value and increment the left index by 1

if nums is empty, return 0 

"""
from typing import List


def remove_duplicates(self, nums: List[int]) -> int:
    lp = 1

    if len(nums) == 0: return 0

    for rp in range(1, len(nums)):
        if nums[rp] != nums[rp - 1]:
            nums[lp] = nums[rp]
            lp += 1
    return lp



print('\n\n')
print("Printing")
print("Result")
print("vs")
print("Expected...\n")

print(remove_duplicates(None, [1, 1, 2]))
print("2\n")

print(remove_duplicates(None, [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print("5\n")

print(remove_duplicates(None, [1, 2, 3, 4, 5]))
print("5\n")

print(remove_duplicates(None, []))
print("0\n")
