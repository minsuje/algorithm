def solution(s):
    #slist = s.split(" ")
   # answer = ""
   # for i in slist:
    #    if i == slist[0]:
    #        answer += i.capitalize()
    #    else:
     #       answer += (" "+ i.capitalize())
    return ' '.join(word.capitalize() for word in s.split(" "))