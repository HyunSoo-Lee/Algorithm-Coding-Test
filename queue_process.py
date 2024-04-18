# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 0
    prior_process = priorities[0]
    i = 0
    while(1):
        print(prior_process)
        if priorities[i] > prior_process:
            prior_process = priorities[i]
            priorities.remove(priorities[i])
        else: i += 1
        print(priorities, i)
    return answer

priorities = [2,1,3,2] #[1,1,9,1,1,1]
location = 2 #0
print(solution(priorities, location))