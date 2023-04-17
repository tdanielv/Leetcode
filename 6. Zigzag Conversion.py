class Solution:
    def convert(self, s: str, numRows: int) -> str:
        t = {}
        l = len(s)
        j = l//(numRows+numRows-2)
        for i in range(numRows):
            t[i] = []
        if numRows < l:
            for k in range(numRows):
                # t[k].append(s[k])
                print(k, s[k])
            for k in range(numRows, l):
                if k <= (2*numRows):
                    i = 2*numRows-k
                    print(i, s[k])
                if (2*numRows)< k <(2*numRows+3):
                    i = 2*numRows-k
                    print(i, s[k])

        return True

print(Solution().convert("PAYPALISHIRING",5))
# print(Solution().convert("PAYPALISHIRING",3), Solution().convert("PAYPALISHIRING",3) == "PAHNAPLSIIGYIR")
# print(Solution().convert("A",1), Solution().convert("A",1) == 'A')