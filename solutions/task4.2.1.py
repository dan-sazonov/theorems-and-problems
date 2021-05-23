# сортировка Хоара, которая эффективнее приведенных в книге

x = list(map(int, input().split()))


def qsort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [j for j in arr[1:] if j > pivot]

    return qsort(less) + [pivot] + qsort(greater)


print(qsort(x))
