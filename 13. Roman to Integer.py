class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        t = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        for i in range(len(s)+1):
            try:
                if int(t[s[i]])< int(t[s[i+1]]):
                    res -= int(t[s[i]])
                else:
                    res += int(t[s[i]])
            except:
                res += int(t[s[i]])
                return res
        return res
# print(Solution().romanToInt("III"))
# assert Solution().romanToInt("III") == 3
# assert Solution().romanToInt("LVIII") == 58
# assert Solution().romanToInt("MCMXCIV") == 1994
# assert Solution().romanToInt()
