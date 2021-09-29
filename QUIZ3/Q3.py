from random import seed, randrange
from collections import Counter


def give_values_to_letters(for_seed):
    seed(for_seed)
    return [randrange(1, 10) for _ in range(26)]


# word and letters are both meant to be strings of nothing but
# uppercase letters, values, a list returned by
# give_values_to_letters(). Returns:
# - -1 if word is not in dictionary.txt
# - 0 if word is in dictionary.txt but cannot be built from letters
# - the value of word according to values otherwise.
def can_be_built_from_with_value(word, letters, values):
    file = open("dictionary.txt")
    dct = file.readlines()
    wd = word + '\n'
    # elements in dct all contain '\n'
    # wd add '\n' to match the format
    if wd in dct:
        counterw = Counter(word)
        counterl = Counter(letters)
        Listw = list(counterw.elements())
        Listl = list(counterl.elements())
        Judg = all(v <= counterl[k] for k, v in counterw.items())
        # Jude is used to judge whether input letters contains all letters to build word
        if Judg:
            sum = 0
            for i in Listw:
                sum = sum + values[ord(i) - 65]
                # use ord()-65 to assign sequence to value
            return sum
        else:
            return 0
    else:
        return -1


# letters is meant to be a string of nothing but uppercase letters.
# Returns the list of words in dictionary.txt that can be built
# from letters and whose value according to values is maximal.
# Longer words come before shorter words.
# For a given length, words are lexicographically ordered.

def most_valuable_solutions(letters, values):
    file = open("dictionary.txt")
    L = file.readlines()
    t = 0;
    S = []
    L = ([' '.join([i.strip() for i in price.strip().split('\n')]) for price in L])
    # remove all '\n' in L, to ease later operations
    counterl = Counter(letters)
    while t < len(L):
        counterL = Counter(L[t])
        Judg = all(v <= counterl[k] for k, v in counterL.items())
        if Judg:
            S.append(L[t])
        t = t + 1
    Y = []
    Z = []
    i = 0
    j = 0
    # Z[] for storing all words in dictionary which can be built with letters
    # Y[] for storing all words of Z[] which has the max value according to values[]
    while (i < len(S)):
        Z.append(calculate(S[i], values))
        i = i + 1
    if Z:
        n = Z.count(max(Z))
        while (j < n):
            t = Z.index(max(Z))
            Y.append(S[t])
            Z.remove(Z[t])
            S.remove(S[t])
            j = j + 1

        Ysort = sorted(Y, key=lambda i: len(i), reverse=True)
        return Ysort
    else:
        return []


# POSSIBLY DEFINE OTHER FUNCTIONS
def calculate(element, values):
    List = list(element)
    sum = 0
    for i in List:
        sum = sum + values[ord(i) - 65]
    return sum
