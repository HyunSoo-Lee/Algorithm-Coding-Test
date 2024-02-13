# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# Test case 1
# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]

# Test case 2
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

def solution(participant, completion):
    # dictionary comprehension
    dict_participant = {i:participant[i] for i in range(len(participant))}
    print(dict_participant)
    
    for i in range(len(completion)):
        failure = [k for k,v in dict_participant.items() if v == completion[i]]
        dict_participant.pop(failure[0])
    answer = list(dict_participant.values())
    return answer[0]
    

print(solution(participant,completion))