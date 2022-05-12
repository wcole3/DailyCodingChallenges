"""
A rule looks like this:

A NE B
This means this means point A is located northeast of point B.

A SW C
means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

A N B
B NE C
C N A
does not validate, since A cannot be both north and south of C.

A NW B
A N B
is considered valid.
"""

import numpy as np

# need to have way to define the directions; will be easier later if
# we separate NS and EW

N = 'N'
S = 'S'
E = 'E'
W = 'W'

direction = {N: (0, 1),
             S: (0, -1),
             E: (1, 0),
             W: (-1, 0)}


def get_deltas(direc):
    d_x = 0
    d_y = 0
    if N in direc:
        d_y += direction[N][1]
    elif S in direc:
        d_y += direction[S][1]
    if E in direc:
        d_x += direction[E][0]
    elif W in direc:
        d_x += direction[W][0]
    return d_x, d_y


# The idea is to walk the rules and create a map of all previsouly encountered
# points and test if the new rule makes sense.

def solution(rules: []):
    # need map to store points
    points = {}
    # loop through rules
    for rule in rules:
        # split rule into destination, source, and direction
        parts = rule.split(" ")
        dest = parts[0]
        direc = parts[1]
        source = parts[2]
        # get the deltas for the direction
        d_x, d_y = get_deltas(direc)
        # first see if the source has been encountered yet
        x_s = 0
        y_s = 0
        if source in points.keys():
            x_s = points[source][0]
            y_s = points[source][1]
        else:
            # should check if dest does exist
            if dest not in points:
                # add the source as zero
                points[source] = (x_s, y_s)
            else:
                # calculate the location of source based off dest
                x_s = points[dest][0] - d_x
                y_s = points[dest][1] - d_y
                points[source] = (x_s, y_s)

        # check if we already have prediction for dest, if not add it
        if dest not in points.keys():
            # use source and deltas to predict the location of the dest
            x_d = x_s + d_x
            y_d = y_s + d_y
            points[dest] = (x_d, y_d)
        else:
            test = points[dest]
            # test x and y separately; test the dot product of scaled vectors
            # special case for source = (0, 0)
            #if points[source][0] == 0 and points[source][1] == 0:
            # do checks normally
            if N in direc and test[1] < points[source][1]:
                return False
            elif S in direc and test[1] > points[source][1]:
                return False
            if E in direc and test[0] < points[source][0]:
                return False
            elif W in direc and test[0] > points[source][0]:
                return False
            # else:
            #     # TODO is this overkill?
            #     # first normalize each vector; adjust source to be relative to the origin
            #     north = (0, 1)
            #     source_adj = (points[source][0] - test[0], points[source][1] - test[1])
            #     # normalize each vector
            #     n_norm = north / np.linalg.norm(north)
            #     s_norm = source_adj / np.linalg.norm(source_adj)
            #     angle = np.degrees(np.arccos(n_norm @ s_norm))
            #     print(rule)
            #     print(test)
            #     print(points[source])
            #     print(angle)

    return True


if __name__ == "__main__":
    test1 = ["A N B", "B NE C", "C N A"]
    print(test1)
    print(solution(test1))
    test2 = ["A NW B", "A N B"]
    print(test2)
    print(solution(test2))
    test3 = ["A N B", "B NW C", "C SE A"]
    print(test3)
    print(solution(test3))
    # this is a limitation or ambiguity
    test4 = ["A N B", "B NW C", "C SE A", "D NE C", "D N A"]
    print(test4)
    print(solution(test4))
