"""
A builder is looking to build a row of N houses that can be of K different colors.
 He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost
 to build the nth house with kth color, return the minimum cost which achieves this goal.
"""
import time


def print_time(t0, t1, opt_str: str = None):
    if opt_str is not None: print(opt_str)
    print(f"Elapsed time since last call: {t1 - t0:0.09f} seconds")


if __name__ == "__main__":
    start = time.perf_counter()
    t = time.perf_counter()
    print_time(start, t)
