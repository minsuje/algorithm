import collections

def solution(participant, completion):
    #count = {}
    #for name in participant:
     #   count[name] = count.get(name,0) +1
    #for name in completion:
     #   count[name] -= 1
    #return [name for name, cnt in count.items() if cnt == 1][0]
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]