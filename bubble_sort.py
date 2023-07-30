import random, copy


# optimized bubble sort
def bubble_sort(arr):
    j = 1
    while j < len(arr):
        sorted = True
        for i in range(len(arr) - j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
        if sorted:
            break
        j += 1


def test():
    L = range(100)
    amount = 10
    arrs = []
    for i in range(100):
        arrs.append([random.choice(L) for _ in range(amount)])

    for i in arrs:
        arr = copy.deepcopy(i)
        bubble_sort(arr)
        if not (arr == sorted(i)):
            print(i)


test()
