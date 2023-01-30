def reverse(x: int) -> int:
    if x > 0:
        x = [i for i in str(x)][::-1]
        return 2**31
    else:
        x = [i for i in str(x * -1)][::-1]
        return -1 * int(''.join(x))

# print(reverse(1534236469))

def findMedianSortedArrays(nums1, nums2):
    l = (sorted(nums1 + nums2))
    return sum(l[len(l)//2-1: len(l)//2 + 1])/2 if len(l) % 2 == 0 else l[len(l)//2]

# print(findMedianSortedArrays([2, 1], [3, 4]))


def intToRoman(num: int) -> str:
    s = ''
    s, num = s + 'M' * (num // 1000), num % 1000

    def func(c: int, l: str, num: int, s) -> int:
        if num >= c:
            s += l
            num -= c
            if num >= c:
                return func(c, l, num, s)
            return num, s
        return num, s

    num, s = func(900, 'CM', num, s)
    num, s = func(500, 'D', num, s)
    num, s = func(400, 'CD', num, s)
    num, s = func(100, 'C', num, s)
    num, s = func(90, 'XC', num, s)
    num, s = func(50, 'L', num, s)
    num, s = func(40, 'XL', num, s)
    num, s = func(10, 'X', num, s)
    num, s = func(9, 'IX', num, s)
    num, s = func(5, 'V', num, s)
    num, s = func(4, 'IV', num, s)
    num, s = func(1, 'I', num, s)
    return s
    return s, num
# print(intToRoman(1969))

def mergeKLists(lists):
    li = []
    for l in lists:
        li += l
    return sorted(li)

# print(mergeKLists([[1,4,5],[1,3,4],[2,6]]))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: ListNode):
        li = []
        def func(lis):
                try:
                    li.append(lis.val)
                    print(li)
                finally:
                    lis.next
                return lis.next
        for l in lists:
            print(l[0])
            l = func(l)
        return sorted(li)
a = Solution()
# print(a.mergeKLists([[1,4,5],[1,3,4],[2,6]]))




