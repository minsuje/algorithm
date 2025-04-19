def solution(array, commands):
    answer = []
    for cmd in commands:
        i,j,k = cmd
        slide = array[i-1:j]
        slide.sort()
        answer.append(slide[k-1])
    return answer