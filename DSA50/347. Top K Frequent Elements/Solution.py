class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result = []
        count_map = {}
        for value in nums:
            # if value in count_map:
            #     count_map[value]=count_map[value]+1
            # else:
            #     count_map[value]=1
            count_map[value]=count_map.get(value,0)+1
        # result_order = [[] for x in range(len(nums))]
        result_order = [[] for _ in range(len(nums)+1)]

        for key,v in count_map.items():
            # result_order[v-1].append(key)
            result_order[v].append(key)
        for i in reversed(result_order)  : #range(len(result_order)-1, -1, -1)
            for x in i:#result_order[i]:
                result.append(x)
                if k == len(result):
                    return result
        return result
