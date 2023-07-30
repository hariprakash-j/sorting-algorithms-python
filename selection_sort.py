import random, copy


def selection_sort(arr):
    current_pos = 0
    smallest_pos = 0
    while current_pos < len(arr):
        i = current_pos + 1
        while i < len(arr):
            if arr[i] < arr[smallest_pos]:
                smallest_pos = i
            i += 1
        if current_pos != smallest_pos:
            arr[current_pos], arr[smallest_pos] = arr[smallest_pos], arr[current_pos]
        current_pos += 1
        smallest_pos = current_pos


def test():
    L = range(100)
    amount = 10
    arrs = []
    for i in range(100):
        arrs.append([random.choice(L) for _ in range(amount)])

    for i in arrs:
        arr = copy.deepcopy(i)
        selection_sort(arr)
        if not (arr == sorted(i)):
            print(i)


test()
