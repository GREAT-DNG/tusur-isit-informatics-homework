import itertools

def linear_search_with_exceptions(arr, target, exceptions = []):
    for i in range(len(arr)):
        if arr[i] == target and i not in exceptions: return i
    return -1

def anagram1(s1, s2):
    if len(s1) != len(s2): return False
    s2 = list(s2)
    marked = []
    for c in s1:
        if c in marked: continue
        pos = linear_search_with_exceptions(s2, c, marked)
        if pos != -1: marked.append(pos)
        else: return False
    return True

def anagram2(s1, s2):
    if len(s1) != len(s2): return False
    return sorted(s1) == sorted(s2)

def anagram3(s1, s2):
    variations = list(itertools.permutations(s1))
    for i in variations:
        if s2 == "".join(i): return True
    return False

def anagram4(s1, s2):
    if len(s1) != len(s2): return False
    c1 = [0] * 26
    c2 = [0] * 26
    for i in s1: c1[ord(i)-97] += 1
    for i in s2: c2[ord(i)-97] += 1
    return c1 == c2

def is_anagram(s1, s2):
    return anagram4(s1, s2)
