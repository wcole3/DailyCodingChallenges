"""
The area of a circle is defined as πr^2. Estimate π to
 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""
import time

# We can estimate pi by inscibing the unit circle inside the
# unit square and randomly dropping dots in the square's area.
# If we compare the ratio of points inside the circle to outside
# we should get an estimate of pi since the area of the unit
# circle is pi and the area of the unit circle is 4; meaning
# the prob. of dropping in the pi/4.


def print_time(t0, t1, opt_str: str = None):
    if opt_str is not None: print(opt_str)
    print(f"Elapsed time since last call: {t1 - t0:0.09f} seconds")


if __name__ == "__main__":
    start = time.perf_counter()
    t = time.perf_counter()
    print_time(start, t)
