"""this is answer
   you know"""
import random


def swap(lyst, a, b):
    a1 = lyst[a]
    lyst[a] = lyst[b]
    lyst[b] = a1


def quick_sort(lyst):
    quick_sort_helper(lyst, 0, len(lyst)-1)


def quick_sort_helper(lyst, left, right):
    if left < right:
        pivot_location = partition(lyst, left, right)
        quick_sort_helper(lyst, left, pivot_location - 1)
        quick_sort_helper(lyst, pivot_location + 1, right)


def partition(lyst, left, right):
    # find thr pivot and exchange it with the last item
    middle = (left + right)//2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # set boundary point to first position
    boundary = left
    # move items less thar pivot to left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary = boundary + 1
    # exchange the pivot item and the boundary item
    swap(lyst, right, boundary)
    return boundary


def main():
    lyst = []
    for count in range(10):
        lyst.append(random.randint(1, 10 + 1))
        print(lyst)
        quick_sort(lyst)
        print(lyst)


if __name__ == '__main__':
    main()

