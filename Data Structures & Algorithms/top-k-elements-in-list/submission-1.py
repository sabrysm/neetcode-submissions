class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # HashMap of num: count then sort by count desc
        answer = []
        num_count_map = defaultdict(int)
        count_num_map = defaultdict(list)
        remaining = k

        for num in nums:
            num_count_map[num] += 1
        
        for num, count in num_count_map.items():
            count_num_map[count].append(num)


        top_k = sorted(set(num_count_map.values()), reverse=True)[:k]
        for top_count in top_k:
            if remaining <= 0:
                break
            size = len(count_num_map[top_count])
            answer.extend(count_num_map[top_count])
            remaining -= size
        
        return answer