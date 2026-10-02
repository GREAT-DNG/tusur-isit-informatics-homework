import random

def insertion_sort(arr):
    new_arr = arr.copy()
    for i in range(1, len(new_arr)):
        j = i
        while j > 0 and (new_arr[j-1] > new_arr[j]):
            new_arr[j-1], new_arr[j] = new_arr[j], new_arr[j-1]
            j -= 1
    return new_arr

def quick_sort(arr):
    if len(arr) < 4: return insertion_sort(arr)
    point = random.choice(arr)
    left = []
    middle = []
    right = []
    for i in arr:
        if i < point: left.append(i)
        elif i > point: right.append(i)
        else: middle.append(i)
    return quick_sort(left) + middle + quick_sort(right)
