"""
Given a stream of elements too large to store in memory,
 pick a random element from the stream with uniform probability.
"""
import time

# My first thought is that you'd want a timer to wait a certain amount of time before returning the chosen element.
# But that seems like it wouldn't be uniform since the you don;t know the amount of time it will take to stream all the
# elements

def print_time(t0, t1, opt_str: str = None):
    if opt_str is not None: print(opt_str)
    print(f"Elapsed time since last call: {t1 - t0:0.09f} seconds")


if __name__ == "__main__":
    start = time.perf_counter()
    t = time.perf_counter()
    print_time(start, t)
