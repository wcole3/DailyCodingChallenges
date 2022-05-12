"""
Given an array of integers, find the first missing positive integer
 in linear time and constant space. In other words, find the lowest
  positive integer that does not exist in the array. The array can
  contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2.
 The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

# first thought is to sort the list in descending order and
# test adjacent points
def solution(input : []):
    # sort list in descending order
    input.sort(reverse=True)
    # go through list and check points on sides
    for i in range(1, len(input)):
        # if this number and previous were negative we can stop looping
        if input[i - 1] < 0 and input[i] < 0:
            break
        if input[i - 1] - input[i] > 1:
            # this value is more than 1 away from previous
            # but we only want positive missing values
            if input[i - 1] - 1 >= 0:
                return input[i - 1] - 1
    # if we get here there were no missing values so the next missing
    # value is based on the first value
    return input[0] + 1
if __name__ == "__main__":
    test = [3, 4, -1, 1, 4, 3, -5]
    print(solution(test))