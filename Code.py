class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        t = sorted(happiness,reverse=True)
        count = 0
        for x in range(k):
            if (t[x]-x)>0:
                count+= t[x]-x
        return count
