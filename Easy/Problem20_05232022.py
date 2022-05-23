"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""
import time
import random as rnd
from LinkedList import SLinkedList


def print_time(t0, t1, opt_str: str = None):
    if opt_str is not None: print(opt_str)
    print(f"Elapsed time since last call: {t1 - t0:0.09f} seconds")


# If the lists intersect there is a sublist common to both lists.  Take advantage of this fact to find the intersection.
# Start by finding the size difference between the two lists.  Then move the longer list to the size difference.  Then
# step through the two lists until the nodes are the same.

def find_intersection(l1: SLinkedList, l2: SLinkedList):
    diff = ll1.size() - ll2.size()
    ptr1 = ll1.headval
    ptr2 = ll2.headval
    if diff > 0:
        # list 1 is bigger
        for _ in range(diff):
            ptr1 = ptr1.nextval
    elif diff < 0:
        # list 2 is bigger
        for _ in range(abs(diff)):
            ptr2 = ptr2.nextval
    # now there are the same number of remaining points, find intersection
    intersection = None
    while ptr1 is not None and ptr2 is not None:
        if ptr1.dataval == ptr2.dataval:
            intersection = ptr1.dataval
            # test that the remaining points match
            while ptr1 is not None and ptr2 is not None:
                if ptr1.dataval != ptr2.dataval:
                    intersection = None
                    break
                ptr1 = ptr1.nextval
                ptr2 = ptr2.nextval
            if ptr1 is None and ptr2 is None:
                return intersection
        ptr1 = ptr1.nextval
        ptr2 = ptr2.nextval



if __name__ == "__main__":
    start = time.perf_counter()
    ll1 = SLinkedList()
    ll1.create_list(reversed([3, 7, 8, 10]))
    ll2 = SLinkedList()
    ll2.create_list(reversed([99, 1, 8, 10]))
    print("Intersection value: ", find_intersection(ll1, ll2))
    t = time.perf_counter()
    print_time(start, t)
    start = time.perf_counter()
    seed = [rnd.randrange(0, 100) for _ in range(10)]
    ll1.create_list(reversed(seed))
    ll2.create_list(reversed([rnd.randrange(0, 100) for _ in range(3)] + seed))
    print("List 1: ")
    ll1.print_list()
    print("List 2: ")
    ll2.print_list()
    print("Intersection value: ", find_intersection(ll1, ll2))
    t = time.perf_counter()
    print_time(start, t)
