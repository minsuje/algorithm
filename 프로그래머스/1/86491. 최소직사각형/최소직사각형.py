def solution(sizes):
    size_sorted=[[max(w,h), min(w,h)] for w,h in sizes]
    max_w = max(size[0] for size in size_sorted)
    max_h = max(size[1] for size in size_sorted)

    return max_w * max_h
