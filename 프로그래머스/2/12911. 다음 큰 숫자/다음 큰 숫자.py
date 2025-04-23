def solution(n):
    count_n = bin(n).count('1')
    next_n = n + 1
    while True:
        if bin(next_n).count('1') == count_n:
            return next_n
        next_n += 1