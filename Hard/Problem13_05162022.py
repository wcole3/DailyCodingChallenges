"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""
import time

# brute force attempt would be to loop through the string, and for each point,
# store the character and test each other encountered point.

# NOTE: This was a wrong solution that found the longest substring with at least k distinct characters.
#  I figured I'd leave it even though there are probably better implementations

def wrong_solution(input : str, k : int):
    found_substrings = []
    i = 0
    while i < len(input) - 1:
        encountered_characters = [input[i]]
        i += 1
        while input[i] not in encountered_characters and i < len(input) - 1:
            encountered_characters.append(input[i])
            i += 1
        if len(encountered_characters) == k:
            found_substrings.append(encountered_characters)
    return max(found_substrings, key=len)


def print_time(t0, t1, opt_str: str = None):
    if opt_str is not None: print(opt_str)
    print(f"Elapsed time since last call: {t1 - t0:0.09f} seconds")


if __name__ == "__main__":
    test1 = "abcba"
    test2 = "abcdefghijklmnopqrstuvwxyz"
    test3 = "abcbhdusbbbsaksdgwkwl"
    start = time.perf_counter()
    print(wrong_solution(test1, 2))
    print(wrong_solution(test2, 3))
    print(wrong_solution(test3, 4))
    t = time.perf_counter()
    print_time(start, t)
