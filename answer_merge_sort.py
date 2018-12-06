"""author: seagal
   time:12.06
   merge sort
   先沿着一条路拆分到单个，然后合并，然后拆分，然后合并，合并的合并
   这个执行顺序 good"""


def merge_sort(list0):
    """博客看的easy"""
    if len(list0) == 1:
        return list0
        # 返回单个的list1， list2
    # 实现不断拆分
    mid = len(list0)//2
    left = list0[:mid]
    right = list0[mid:]
    print('拆分')
    print('left:', left)
    print('right:', right)
    list1 = merge_sort(left)
    list2 = merge_sort(right)
    # 必须等前边的拆分完才可以组合
    print('排序合并')
    # 合并后返回正确排序的子列表是怎么循环迭代？？
    # 为毛有两个子列表会自动排序合并?
    # 和前边的list1 list2 有种莫名的对应，拆分成单个的list1 list2，是由上层list1拆的
    # 合并之后返回了list1? 然后另一个上层的list2开始拆分成list1 list2，合并后返回list2，
    # 因为函数还没有结束，所以可以接着合并上层的list1 list2， 返回上上层list1
    # 还是不明白他本身返回的不是list1， list2啊，为毛还能接着合并? 迭代？
    # # # 还是说，运行是每次都应该从头运行到结尾，merge每次都想合并，但是让上边的迭代完把，然后他开始干他合并list1 list2的活
    # # # 的但是应该先把上边两个递归完， 然后他再执行， 区别就是list的顺序发生了变化，list还是那个list
    # # # 核心就是 接受一个list 分为两个list 然后排序合并成一个list， 这就是merge_sort的真意，相当于给merge_sort输入一个返回一个
    # print(merge(list1, list2)) 这个会影响返回结果
    return merge(list1, list2)


def merge(l1, l2):
    """对拆分的列表排序，然后合并"""
    print('合并列表')
    print('l1:', l1)
    print('l2:', l2)
    result = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] <= l2[0]:
            result.append(l1.pop(0))
        else:
            result.append(l2.pop(0))
    # while 执行结束必定会有一个耗尽
    result = result + l1
    result = result + l2
    # 因为循环是拆成单个，然后开始排序，合并，所以每个列表都是升序的
    # 这个是最后返回的
    print('合并结果', result)
    return result


if __name__ == '__main__':
    list_test = [9, 3, 2, 1, 5, 7, 6, 4]
    print(merge_sort(list_test))