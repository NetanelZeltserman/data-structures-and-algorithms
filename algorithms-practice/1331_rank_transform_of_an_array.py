from typing import List


def array_rank_transform(arr: List[int]) -> List[int]:
    # arr = [6,7,2]
    value_to_rank = {}  # Dictionary to store value-to-rank mapping
    sorted_unique_numbers = sorted(list(set(arr)))  # Remove duplicates and sort unique elements
    # sorted_unique_numbers = [2,6,7]

    # Assign ranks to sorted unique elements
    for index in range(len(sorted_unique_numbers)): 
        value_to_rank[sorted_unique_numbers[index]] = index + 1
        # value_to_rank = {
        #   2: 10,
        #   6: 20,
        #   7: 30
        # }

    # Replace each element in the original array with its rank
    for index in range(len(arr)): 
        arr[index] = value_to_rank[arr[index]]
        # foreach value, find rank in value_to_rank
        #   set to num's index value

        # so if arr[index] is 2, the value in arr
        # will be replaced to 10

        # and so, we could've ignored duplicates in the first loop,
        # because same numbers will have the same value.
        # and here we just get the value based on the number's "reference"

    return arr  # Return the updated array


print(array_rank_transform([40, 10, 20, 30]))
print([4, 1, 2, 3])

print(array_rank_transform([100, 100, 100]))
print([1, 1, 1])

print(array_rank_transform([37, 12, 28, 9, 100, 56, 80, 5, 12]))
print([5, 3, 4, 2, 8, 6, 7, 1, 3])
