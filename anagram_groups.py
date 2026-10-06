def largest_anagram_group(words):
    groups = {}
    for i in words:
        i_sorted = "".join(sorted(i))
        if i_sorted not in groups:
            groups[i_sorted] = []
        groups[i_sorted].append(i)
    max_group = []
    max_len = -1
    for i in groups:
        if len(groups[i]) > max_len and len(groups[i]) > 1:
            max_group = groups[i]
            max_len = len(groups[i])
    return sorted(max_group)
