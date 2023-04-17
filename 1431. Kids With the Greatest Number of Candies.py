class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        r = True
        w = []
        res = []
        for i in range(len(candies)):
            for j in range(len(candies)):
                if i != j:
                    if candies[i]+extraCandies >= candies[j]:
                        w.append(True)
                    else:
                        w.append(False)

            if False in w:
                res.append(False)
            else:
                res.append(True)
            w = []
        return res

print(Solution().kidsWithCandies([2,3,5,1,3], 3))