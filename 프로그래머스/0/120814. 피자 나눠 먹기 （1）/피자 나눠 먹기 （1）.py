def solution(n):
    pizza = 1
    while True :
        slices = pizza * 7
        if slices >= n :
            return pizza
        pizza += 1