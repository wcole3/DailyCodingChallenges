"""
Implement an autocomplete system. That is, given a query
 string s and a set of all possible query strings, return
  all strings in the set that have s as a prefix.

For example, given the query string de and the set of
 strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more
 efficient data structure to speed up queries.
"""
import time


def print_time(t0, t1, opt_str: str = None):
    if opt_str is not None: print(opt_str)
    print(f"Elapsed time since last call: {t1 - t0:0.09f} seconds")


# The brute force approach would be to loop over the list
# of possibilities and check if current input exists in
# any the elements


def brute_force(input_string: str, input_words=[]):
    hits = []
    for word in input_words:
        if input_string == word[0:len(input_string)]:
            hits.append(word)

    return hits


def process_words(input_words: []):
    # To speed up lookup we can process the results into a dict
    d = {}
    for word in input_words:
        for i in range(len(word)):
            if word[0:i] in d.keys():
                d[word[0:i]].append(word)
            else:
                d[word[0:i]] = [word]
    return d

# define these outside to isolate timings
words = ["dog", "deer", "deal", "camel", "worried", "typical", "destitute", "deescalate", "simply"]
processed_words = process_words(words)

if __name__ == "__main__":
    start = time.perf_counter()
    # brute force case
    print(brute_force("de", words))
    print(brute_force("s", words))
    print(brute_force("dee", words))
    t = time.perf_counter()
    print_time(start, t, "Brute force case:")
    start = t
    # preprocessed case
    print(processed_words["de"])
    print(processed_words["s"])
    print(processed_words["dee"])
    t = time.perf_counter()
    print_time(start, t, "Preprocessed case:")
