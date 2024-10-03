"""
create a pointer (k) that will be incremented for each value that is not 'val',
and will indicate that the current element (i) should be replaced with that value

then loop through the elements in nums, when the current value is not 'val', replace it with the element in position 'k'
"""

from typing import List

def remove_element(nums: List[int], val: int) -> int:
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

print('\n\n')
print(remove_element([3,2,2,3], 3))
print(2)
print('\n')

print(remove_element([0,1,2,2,3,0,4,2], 2))
print(5)
print('\n')

print(remove_element([1], 1))
print(0)
print('\n')

print(remove_element([], 1))
print(0)
print('\n')

print(remove_element([1,1,1,1,1], 1))
print(0)
