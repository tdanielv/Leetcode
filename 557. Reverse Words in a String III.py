class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        l2 = []
        for j in l:
            l2.append(j[::-1])
        return ' '.join(l2)