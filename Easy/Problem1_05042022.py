'''
Daily coding problem from 05042022

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''


# Naive first approach would be to generate all possible combinations
# could improve by only calc non-deg combos
# could loop through once; subtract number from target and search through hash if diff is in it (1 -pass)

def has_sum(nums : set, target: int):
    for num in nums:
        test = target - num
        if num > 0 and test in nums:
            return True
    return False


if __name__ == "__main__":
    nums = set([10, 15, 3, 7])
    target = 17
    print(has_sum(nums, target))
