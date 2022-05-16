"""
Given a list of integers, write a function that returns the
 largest sum of non-adjacent numbers. Numbers can be 0 or
  negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick
 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick
  5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

import sys
import itertools as it

# The brute force should be straightforward to loop through
# the list and find all the non-adjacent indices for each
# index. Then brute force through all of the possible
# combinations


def brute_force(nums : []):
    max_sum = -1 * sys.maxsize
    for length in range(len(nums)):
        # get all possible combinations of the indices
        combos = list(it.combinations(list(range(len(nums))), length))
        # now go through all combinations and calculate the sum if non of the indices are adjacent
        for combo in combos:
            # first check that this combo is valid
            valid = True
            for i in combo:
                if i - 1 in combo or i + 1 in combo:
                    valid = False
            if valid:
                test_total = 0
                for i in combo:
                    test_total += nums[i]
                max_sum = test_total if test_total > max_sum else max_sum
    return max_sum


# It feels like there should be a graph/node solution to this.
# Each index is a node with the child nodes being the non-adj
# nodes.  Then you step through all possible paths of the tree
# and return the max value.  That doesn't seem like i'd be o(n)
# though so I doubt thats a good solution.

if __name__ == "__main__":
    test1 = [2, 4, 6, 2, 5]
    print(brute_force(test1))
    test2 = [5, 1, 1, 5]
    print(brute_force(test2))
    test3 = [-3, 1, 6, 4, 6, 9]
    print(brute_force(test3))
    test4 = [-3, 1, 0, 4, 6, 9]
    print(brute_force(test4))