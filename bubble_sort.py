"""author: seagal
   time : 12.03
   bubble sort"""


def bubble_sort(list0):
    n = len(list0)
    while n > 1:
        for i in range(0, n-1):
            if list0[i] > list0[i+1]:
                c = list0[i]
                list0[i] = list0[i+1]
                list0[i+1] = c
        # 这个n在while下边， 不是for 下边
        n = n - 1
    return list0


list1 = [9, 3, 2, 1, 5, 7, 6, 4]
test = bubble_sort(list1)
print(test)

