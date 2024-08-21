# 해시 > 완주하지 못한 선수
# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter

# Test case 1
# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]

# Test case 2
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

# 접근 방법
# participant 리스트를 딕셔너리화
# completion 리스트와 비교
# runner 리스트를 만들어야 하나요?


# def solution(participant, completion):
    # # dictionary comprehension -> '번호 : 참가자' 딕셔너리 생성 
    # dict_participant = {i:participant[i] for i in range(len(participant))}
    # print(dict_participant)
    
    # for i in range(len(completion)):
    #     # O(n^2) 발생 지점. 고쳐야 함
    #     # participant 딕셔너리와 completion 리스트에 동시에 들어가있는 러너 찾기
    #     # 동시에 들어있는 러너의 인덱스 번호를 runner 리스트 내에 삽입
    #     runner = [k for k,v in dict_participant.items() if v == completion[i]]
    #     print(runner)
    #     # 딕셔너리에서 해당 번호 팝
    #     dict_participant.pop(runner[0])
    # answer = list(dict_participant.values())
    # return answer[0]

def solution(participant, completion):
    dict_participant = {}
    #딕셔너리의 경우 key - value에서 사칙연산 사용 가능
    for p in participant:
        if p in dict_participant:
            dict_participant[p] += 1
        else:
            dict_participant[p] = 1
    print(dict_participant)

    for c in completion:
        if c in dict_participant:
            dict_participant[c] -= 1
    #print(dict_participant)
    
    for k,v in dict_participant.items():
        if v > 0:
            return k

def answer(participant, completion):
    participant_counter = Counter(participant)
    #print(participant_counter)
    completion_counter = Counter(completion)
    #print(completion_counter)

    diff = participant_counter - completion_counter
    #print(diff)
    return list(diff.keys())[0]
    

print(solution(participant,completion))
#print(answer(participant,completion))