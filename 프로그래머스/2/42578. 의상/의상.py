def solution(clothes):
    count = {}
    for stuff, part in clothes:
        count[part] = count.get(part, 0) +1
    
    answer = 1
    for num in count.values():
        answer *= (num+1)
    answer -= 1
    return answer