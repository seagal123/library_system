"""author: seagal
   time: 12.04
   quick sort"""


def quick_sort(list0):
    """快速排序，可以考虑递归实现"""
    pivot = len(list0)//2 - 1
    print(list0[pivot], pivot)
    # 基准点和最右边互换
    c = list0[pivot]
    list0[pivot] = list0[-1]
    list0[-1] = c
    # 最左边插入边界,这个边界不用在列表里边，无形的更好操作
    n = 0
    list0.insert(n, 'border')
    # 遍历并移动边界
    for i in range(1, len(list0)-1):
        # 如果小于基准点和边界后边一位互换，移动边界
        if list0[i] < list0[-1]:
            d = list0[i]
            list0[i] = list0[n+1]
            list0[n+1] = d
            # 移动边界
            e = list0[n]
            list0[n] = list0[n+1]
            list0[n+1] = e
            # 这么做不会干扰i 后边的值，所以for 循环不用修改?
            n = n + 1

    list0[n] = list0[-1]
    list0.pop()
    print(list0)
    # 长度大于等于2继续进行切割
    if len(list0) > 2:
        if n < len(list0)-1:
            print('a')
            list3 = list0[0:n+1]
            list2 = list0[n+1:]
            # 这两个函数的先后顺序迭代有什么区别?
            quick_sort(list3)
            quick_sort(list2)
            # return list2, list3
        if n == len(list0)-1:
            print('b')
            list3 = list0[0:n+1]
            quick_sort(list3)
            # return list3
    else:

        return 'over'


list1 = [9, 3, 2, 1, 5, 7, 6, 4]
# 如果想这样直接赋给test， 则必须有return， 否则直接quick_sort(list1)就行了
test = quick_sort(list1)
print(test)





