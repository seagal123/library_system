"""author:
   time: 12.06
   fib for loop implementation"""


def fib(n):
    """for loop"""
    # 尽量不要用内置的函数名称
    total = 1
    first = 1
    second = 1
    count = 3
    while n < count:
        return total
    while count <= n:
        total = first + second
        first = second
        second = total
        count = count + 1
    return total


print(fib(2))
