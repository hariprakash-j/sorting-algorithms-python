import math
import random


def merge(arr1, arr2):
    i = 0
    j = 0
    arr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] >= arr2[j]:
            arr.append(arr2[j])
            j += 1
        elif arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
    if i <= len(arr1) - 1:
        arr = arr + arr1[i:]
    elif j <= len(arr2) - 1:
        arr = arr + arr2[j:]
    return arr


def merge_sort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    mid = round(len(arr) / 2)
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def test():
    L = range(100)
    amount = 10000
    arrs = []
    for i in range(100):
        arrs.append([random.choice(L) for _ in range(amount)])

    for i in arrs:
        assert merge_sort(i) == sorted(i)


test()
