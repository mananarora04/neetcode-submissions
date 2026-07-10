class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for i in nums:
            hashmap[i]=1+hashmap.get(i,0)

        arr=[]
        for i,j in hashmap.items():
            arr.append([j,i])
        arr.sort()

        res=[]

        while len(res)<k:
            last = arr.pop()
            res.append(last[1])
        return res