def solution(nums):
    num_max = len(nums)//2 # 최대 선택 2개
    poketmons = len(set(nums)) # 3종류
    
    return min(num_max, poketmons)