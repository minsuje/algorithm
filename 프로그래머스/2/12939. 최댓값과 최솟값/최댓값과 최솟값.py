def solution(s):
    r = s.split(' ')
    nums = [int(i) for i in r]
    nums.sort()
    answer = f"{nums[0]} {nums[-1]}"
    return answer