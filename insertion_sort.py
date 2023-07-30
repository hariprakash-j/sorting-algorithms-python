import random, copy


def insertion_sort(arr):
    sorted_pos = 0
    i = sorted_pos + 1
    while i < len(arr):
        j = sorted_pos
        while j >= 0:
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
            i = j
            j -= 1
        sorted_pos += 1
        i = sorted_pos + 1


def test():
    L = range(100)
    amount = 10
    arrs = []
    for i in range(100):
        arrs.append([random.choice(L) for _ in range(amount)])

    for i in arrs:
        arr = copy.deepcopy(i)
        insertion_sort(arr)
        if not (arr == sorted(i)):
            print(i)


test()
