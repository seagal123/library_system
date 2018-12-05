"""author:seagal
   time:13
   可以考虑一下迭代实现"""


def selection_sort(list0):
    """selection sort"""
    n = 0
    while n < len(list0) - 1:
        min = list0[n]
        min_index = n
        for i in range(n + 1, len(list0)):
            if min > list0[i]:
                # 是i 不是1，看清楚， 或者少用这个符号
                min = list0[i]
                min_index = i
        # 这个值不会变，因为直接传的是值，如果c = list0，则会变
        c = list0[n]
        list0[n] = min
        list0[min_index] = c
        n = n + 1


list1 = [3, 2, 1, 5, 7, 6]
selection_sort(list1)
print(list1)


