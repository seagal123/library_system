"""author: seagal
   time: 12.04
   quick sort
   迭代输出把一个一直迭代完了再迭代另一个？
   再多一个left，一个right就不用真正的切开了,nb"""


def swap(list0, a, b):
    c = list0[a]
    list0[a] = list0[b]
    list0[b] = c


def quick_sort(list0, left, right):
    """快速排序，可以考虑递归实现"""
    # left = 0
    # right = len(list0) - 1
    pivot = (left + right)//2
    print('排序前', list0)
    dd = list0[pivot]
    print('基准点', list0[pivot])
    # 基准点和最右边互换
    swap(list0, pivot, right)
    # 最左边插入边界,这个边界不用在列表里边，无形的更好操作
    boundary = left
    # border = n
    # 遍历并移动边界
    for i in range(left, right):
        # 如果小于基准点和边界后边一位互换，移动边界
        if list0[i] < dd:
            swap(list0, boundary, i)
            # 移动边界
            boundary = boundary + 1

    # 基准点和边界互换
    swap(list0, boundary, right)
    print('排序后', list0)
    return boundary
    # 构造辅助函数和直接表达的区别， 为啥直接表达不对，还是各种变量传值传引用的问题
    # if right - left > 0:
        # quick_sort(list0, left, boundary-1)
        # quick_sort(list0, boundary+1, right)


def quick_sort_helper(list0, left, right):
    if left < right:
        pivot_location = quick_sort(list0, left, right)
        quick_sort_helper(list0, left, pivot_location-1)
        quick_sort_helper(list0, pivot_location+1, right)


list1 = [9, 3, 2, 1, 5, 7, 6, 4]
# 如果想这样直接赋给test， 则必须有return， 否则直接quick_sort(list1)就行了
quick_sort_helper(list1, 0, len(list1)-1)
print(list1)
# 啥都没有的list长度为0
# print(len([]))





