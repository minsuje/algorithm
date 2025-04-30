def solution(brown, yellow):
    
    # brown  = (width*2)+(hight*2) - 4
    # yellow = (width-2)*(hight-2)
    # width + hight = total
    # total == (width + 4) // 2
    total = brown + yellow
    for hight in range(3, int(total**0.5) + 1):
        if total % hight == 0:
            width = total // hight
            if width >= hight and (width-2)*(hight-2) == yellow:
                return [width, hight]
                    