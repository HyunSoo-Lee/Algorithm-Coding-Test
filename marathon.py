# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# Test case 1
# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]

# Test case 2
# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]

# Test case 3
# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]

# Test case 4
participant = ["leo"]
completion = []

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    # print(participant)
    # print(completion)
    if len(completion) > 0:
        for i in range(len(completion)):
            if participant[i] != completion[i]:
                answer = participant[i]
                quit
            elif i == len(completion) - 1:
                answer = participant[i+1]
                quit
    else:
        answer = participant[0]
    return answer

print(solution(participant, completion))