def solution(numbers):
    nums = list(map(str,numbers))
    nums.sort(key=lambda x: x*3, reverse=True)
    answer = ''.join(nums)
    return answer if answer[0] != '0' else '0'