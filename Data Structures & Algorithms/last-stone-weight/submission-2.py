class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        if len(stones) < 1:
            return 

        while len(stones) > 1:
            maxxie1 = max(stones)
            stones.remove(maxxie1)
            maxxie2 = max(stones)
            stones.remove(maxxie2)
            if maxxie1 == maxxie2:
                continue
            elif maxxie1 < maxxie2:
                stones.append(maxxie2 - maxxie1)
            else:
                stones.append(maxxie1 - maxxie2)
        return stones[0] if len(stones) > 0 else 0
        