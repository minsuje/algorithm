def solution(n, k):
    stick = 12000 * n
    drink = 2000 * k
    free = (n // 10) * 2000
    return stick + (drink - free)