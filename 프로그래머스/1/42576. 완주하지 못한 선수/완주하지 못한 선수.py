def solution(participant, completion):
    participant.sort()
    completion.sort()
    for name, name2 in zip(participant, completion):
        if name != name2:
            return name
    return participant[-1]
    