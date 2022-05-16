"""
There exists a staircase with N steps, and you can climb
 up either 1 or 2 steps at a time. Given N, write a
  function that returns the number of unique ways you
   can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a
 time, you could climb any number from a set of positive
  integers X? For example, if X = {1, 3, 5}, you could
   climb 1, 3, or 5 steps at a time.

There is an implicit assumption in the setup that you don't
 have to land exactly on the last step.
"""
import time


def print_time(t0, t1, opt_str: str = None):
    if opt_str is not None: print(opt_str)
    print(f"Elapsed time since last call: {t1 - t0:0.09f} seconds")


# The first case is the fibonacci seq since we want to find all of the ways of summing
# to a number by 1's and 2's
fib_dict = {0: 1,
            1: 1}


def fibonacci(i: int):
    if i < 0:  # problem statement says this won't happen, but why not add it
        return -1
    if i not in fib_dict.keys():
        val = fibonacci(i - 1) + fibonacci(i - 2)
        fib_dict[i] = val
    return fib_dict[i]


# The general case uses the same logic; if you can take [x_o, ... , x_m]
# steps at a time and you start at the top step (n) you know that that
# step can be reached from steps [n - x_o, ... , n - x_m].  If the
# problem is reconsidered from any of those steps then the logic repeats

gen_dict = {}


def general_case(n: int, steps: []):
    if n < 0:
        return 1
    if n not in gen_dict.keys():
        for i in range(2, n + 1):
            total = 0
            for k in steps:
                total += general_case(i - k, steps)
            gen_dict[i] = total
    return gen_dict[n]


if __name__ == "__main__":
    start = time.perf_counter()
    print(fibonacci(4))
    print(fibonacci(14))
    t = time.perf_counter()
    print_time(start, t, "Base case:")
    start = t
    steps = [1, 2]
    # reset dict
    gen_dict = {0: 1, 1: 1}
    print(general_case(4, steps))
    gen_dict = {0: 1, 1: 1}
    print(general_case(14, steps))
    t = time.perf_counter()
    print_time(start, t, "General case test with fibonacci:")
    start = t
    t = time.perf_counter()
    steps = [2, 4, 5]
    gen_dict = {0: 1, 1: 1}
    print(general_case(4, steps))
    gen_dict = {0: 1, 1: 1}
    print(general_case(14, steps))
    print_time(start, t, "General case:")
