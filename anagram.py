def is_anagram(s1, s2):
    if len(s1) != len(s2): return False
    c1 = [0] * 26
    c2 = [0] * 26
    for i in s1: c1[ord(i)-97] += 1 # pyright: ignore
    for i in s2: c2[ord(i)-97] += 1 # pyright: ignore
    return c1 == c2
