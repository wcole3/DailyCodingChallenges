"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""
import sys
import time


# brute force attempt would be to loop through the string, and for each point,
# store the character and test each other encountered point.

def find_longest_substring(input_str: str, k: int):
    found_substrings = []
    max_size = -1 * sys.maxsize
    for i in range(len(input_str)):
        size = 1
        encountered_chars = set(input_str[i])
        for j in range(i + 1, len(input_str)):
            if len(encountered_chars) >= k and input_str[j] not in encountered_chars:
                break
            else:
                size += 1
                encountered_chars.add(input_str[j])
        if size > max_size:
            max_size = size
    return max_size


def print_time(t0, t1, opt_str: str = None):
    if opt_str is not None: print(opt_str)
    print(f"Elapsed time since last call: {t1 - t0:0.09f} seconds")


if __name__ == "__main__":
    test1 = "abcba"
    test2 = "abcdefghijklmnopqrstuvwxyz"
    test3 = "abcbhdusbbbsaksdgwkwl"
    start = time.perf_counter()
    print(find_longest_substring(test1, 2))
    print(find_longest_substring(test2, 2))
    print(find_longest_substring(test3, 2))
    t = time.perf_counter()
    print_time(start, t)
