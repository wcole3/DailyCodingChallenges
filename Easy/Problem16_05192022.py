"""
You run an e-commerce website and want to record the last N order
 ids in a log. Implement a data structure to accomplish this,
  with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is
 guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""
import time


def print_time(t0, t1, opt_str: str = None):
    if opt_str is not None: print(opt_str)
    print(f"Elapsed time since last call: {t1 - t0:0.09f} seconds")


if __name__ == "__main__":
    start = time.perf_counter()
    t = time.perf_counter()
    print_time(start, t)
