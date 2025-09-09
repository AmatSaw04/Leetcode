class Solution:
    def combinationSum(self, candidates: List[int], tar: int) -> List[List[int]]:
            
        a = []

        def make_comb(idx, comb, tot):
            if tot == tar:
                a.append(comb[:])
                return
            
            if tot > tar or idx >= len(candidates):
                return
            
            comb.append(candidates[idx])
            make_comb(idx, comb, tot + candidates[idx])
            comb.pop()
            make_comb(idx+1, comb, tot)

            return a

        return make_comb(0, [], 0)