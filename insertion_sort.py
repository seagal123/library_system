"""author: seagal
   time : 12.03
   insertion sort"""


def insertion_sort(list0):
    listn = []
    for j in range(0, len(list0)):
        if not listn:
            listn.append(list0[j])
        elif list0[j] >= listn[-1]:
            listn.insert(-1, list0[j])
        elif list0[j] <= listn[0]:
                listn.insert(0, list0[j])
        else:
            for k in range(len(listn)-1):
                if listn[k] <= list0[j] <= listn[k+1]:
                    listn.insert(k+1, list0[j])
                    # 这个要加上， 不然每个循环都会判断，造成一个元素出现几次
                    break

    return listn


list1 = [9, 3, 2, 1, 5, 7, 6, 4, 8]
test = insertion_sort(list1)
print(test)









