# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 0
    process = []
    for i in range(len(priorities)):
        process.append(i)
    i = 0
    while(1):
        maximum = max(priorities)
        if maximum == -1:
            break
        if priorities[0] != maximum:
            priorities.append(priorities[0])
            process.append(process[0])
            priorities.remove(priorities[0])
            process.remove(process[0])
        else:
            priorities[0] = -1
            priorities.append(priorities[0])
            process.append(process[0])
            priorities.remove(priorities[0])
            process.remove(process[0])  
        print(i)
        print(priorities)
        print(process) 
        print('-----')
        i += 1
    answer = process.index(location) + 1
    return answer

priorities = [2,3,1,2]
location = 3
# 기대값 2
# priorities = [2,1,3,2]
# location = 2
# 기대값 1
print('answer = ', solution(priorities, location))