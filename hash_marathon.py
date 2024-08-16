# 해시 > 완주하지 못한 선수
# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# Test case 1
# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]

# Test case 2
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

# 접근 방법
# participant 리스트를 딕셔너리화
# completion 리스트와 비교
# failure 리스트를 만들어야 하나요?


def solution(participant, completion):
    # dictionary comprehension
    dict_participant = {i:participant[i] for i in range(len(participant))}
    print(dict_participant)
    
    for i in range(len(completion)):
        # O(n^2) 발생 지점. 고쳐야 함
        failure = [k for k,v in dict_participant.items() if v == completion[i]]
        dict_participant.pop(failure[0])
    answer = list(dict_participant.values())
    return answer[0]
    

print(solution(participant,completion))