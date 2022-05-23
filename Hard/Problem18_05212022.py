"""
Given an array of integers and a number k, where 1 <= k <= length of the array,
 compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get:
 [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place
 and you do not need to store the results. You can simply print them out as
  you compute them.
"""
import time


def print_time(t0, t1, opt_str: str = None):
    if opt_str is not None: print(opt_str)
    print(f"Elapsed time since last call: {t1 - t0:0.09f} seconds")


if __name__ == "__main__":
    start = time.perf_counter()
    t = time.perf_counter()
    print_time(start, t)