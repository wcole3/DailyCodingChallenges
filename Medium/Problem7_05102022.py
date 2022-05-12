"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
 count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be
 decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example,
 '001' is not allowed.
"""

# we need to find the ambigious sections of the input
# ambig sections start with 1,2 and end with a value > 2 (or end of string)
# special case if prev number in amg section is 2 then value greater than 6
# means the prev 2 is not ambig
# The total number of permutations of decoded string is equal
# to the product of the perm. of each ambig section
# for example,
"""
the string 145781242826 has the following ambig sections

(a)14-578-(a)124-28-(a)26

the perms would be 2 x 3 x 2 = 12

to count the number of permutations we just need to count how many 
valid pairs there are, but we can take advantage of the fact that
the last value will be >
"""
import string

fib_dict = {0: 1,
            1: 1}


def fib(num: int):
    if num < 0:
        return -1
    if num in fib_dict.keys():
        return fib_dict[num]
    else:
        fib_dict[num] = fib(num - 2) + fib(num - 1)
        return fib_dict[num]


# we dont really need a key, but it would be nice for visualization
mapping = dict(zip(range(1, 27), string.ascii_lowercase))


def solution(seq: int):
    chars = str(seq)
    # find amb seqences
    amb_seqs = []
    current_seq = ""
    i = 0
    while i < len(chars):
        val = int(chars[i])
        # check if this the possible start of an amb_seq
        if val < 3:
            # could be a amb_seq
            current_seq += chars[i]
            # go to the end of the amb seq
            i += 1
            looking = True
            while looking and i < len(chars):
                val = int(chars[i])
                if val > 2:
                    # end of ambiguity, check special case
                    if int(chars[i - 1]) == 2:
                        if val < 7:
                            current_seq += chars[i]
                            amb_seqs.append(current_seq)
                            current_seq = ""
                            i += 1
                            looking = False
                        else:
                            if len(current_seq) > 1:
                                amb_seqs.append(current_seq)
                            current_seq = ""
                            i += 1
                            looking = False
                    else:
                        current_seq += chars[i]
                        amb_seqs.append(current_seq)
                        current_seq = ""
                        i += 1
                        looking = False
                else:
                    current_seq += chars[i]
                    i += 1
            # check to make sure we got the last seq
            if len(current_seq) > 1:
                amb_seqs.append(current_seq)
                current_seq = ""
        else:
            i += 1
    print(amb_seqs)
    # count permutations for each amb; this is just Fibonacci!
    total_perm = 1
    for seq in amb_seqs:
        total_perm *= fib(len(seq))
    # return total permutations
    return total_perm


if __name__ == "__main__":
    test1 = 111
    print(solution(test1))
    test2 = 145781242826
    print(solution(test2))
    test3 = 17583927565216193748221212127346192748
    print(solution(test3))
