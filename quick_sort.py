"""author: seagal
   time: 12.04
   quick sort
   迭代输出把一个一直迭代完了再迭代另一个？
   再多一个left，一个right就不用真正的切开了,nb"""


def swap(list0, a, b):
    c = list0[a]
    list0[a] = list0[b]
    list0[b] = c


def quick_sort(list0):
    """快速排序，可以考虑递归实现"""
    pivot = len(list0)//2
    print('排序前', list0)
    print('基准点', list0[pivot])
    # 基准点和最右边互换
    swap(list0, pivot, -1)
    # 最左边插入边界,这个边界不用在列表里边，无形的更好操作
    n = 0
    # border = n
    # 遍历并移动边界
    for i in range(0, len(list0)-1):
        # 如果小于基准点和边界后边一位互换，移动边界
        if list0[i] < list0[-1]:
            swap(list0, n, i)
            # 移动边界
            n = n + 1

    # 基准点和边界互换
    swap(list0, n, -1)
    print('排序后', list0)
    # 长度大于等于2继续进行切割
    if len(list0) >= 2:
        if n < len(list0)-1:
            print('a')
            list3 = list0[0:n]
            list2 = list0[n+1:]
            print('分割1', list3)
            print('分割2', list2)
            if len(list3) >= 2:
                quick_sort(list3)
            if len(list2) >= 2:
                quick_sort(list2)
            # 这两个函数的先后顺序迭代有什么区别?
            # quick_sort(list3)
            # quick_sort(list2)
            # return list2, list3
        if n == len(list0)-1:
            print('b')
            list3 = list0[0:n]
            quick_sort(list3)
            # return list3
    else:

        return 'over'


list1 = [9, 3, 2, 1, 5, 7, 6, 4]
# 如果想这样直接赋给test， 则必须有return， 否则直接quick_sort(list1)就行了
test = quick_sort(list1)
print(test)
# 啥都没有的list长度为0
print(len([]))





