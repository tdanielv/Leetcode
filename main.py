#
#
# def func(s : str):
#     l = s.split(' ')
#     x1, x2, bab = int(l[0]), int(l[1]), 0
#     def dogoni(x1,  x2, bab, step=0, c = False):
#         if x1 > 0:
#             x1 += 1
#             bab += 2
#         else:
#             x1 -= 1
#             bab -= 2
#         if x2 > 0:
#             x2 += 1
#         else:
#             x2 -= 1
#         step += 2
#         if x1 != bab:
#             return dogoni(x1, x2, bab, step, c)
#         elif c == True:
#             return step
#         else:
#             c = True
#             return dogoni(x2, x1, bab, step, c)
#     return dogoni(x1, x2, bab=0)
#
# print(func('-3 -6'))


# s = [i for i in input().split()[0]]
s = [i for i in 'hello3(world)hi'.split()[0]]
i = 0
print(s)
def find_numb(l):
    try:
        res = int(l[0])
        print(l[0], '---')
        return res
    except:
        return False
def find(l):
    for i in range(len(l)):
        if find_numb(l[i:]):
            print(find(s[(i + 2):]), 12)
        if l[i] ==')':
            return l[:i]

while i <= len(s):
    k = find_numb(s[i:])
    if k:
         print(k * find(s[(i+2):]))
    i += 1
    print(i)
