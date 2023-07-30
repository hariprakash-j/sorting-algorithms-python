import random
import copy


def pviot(arr, start=0, end="na"):
    if end == "na":
        end = len(arr) - 1
    pviot = start
    swapidx = start
    i = start
    while i <= end:
        if arr[pviot] > arr[i]:
            swapidx += 1
            arr[swapidx], arr[i] = arr[i], arr[swapidx]
        i += 1

    arr[pviot], arr[swapidx] = arr[swapidx], arr[pviot]

    return swapidx


def quick_sort(arr, start=0, end="na"):
    if end == "na":
        end = len(arr) - 1
    if end <= start:
        return
    pvi = pviot(arr, start, end)
    quick_sort(arr, start, end=pvi - 1)
    quick_sort(arr, pvi + 1, end)


def test():
    L = range(100)
    amount = 10
    arrs = []
    for i in range(100):
        arrs.append([random.choice(L) for _ in range(amount)])

    for i in arrs:
        arr = copy.deepcopy(i)
        quick_sort(arr)
        if not (arr == sorted(i)):
            print(i, sorted(i), arr)


test()
