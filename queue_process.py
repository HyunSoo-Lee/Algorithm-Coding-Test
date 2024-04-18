# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 0
    prior_process = priorities[0]
    i = 0
    while(1):
        print(priorities[i], i)
        if priorities[i] > prior_process:
            prior_process = priorities[i]
            priorities.remove(priorities[i])
            answer += 1
        elif i < len(priorities) - 1: i += 1
        else : 
            if i != location:
                # 여기서부터 다시 시작, len(priorities)보다 적으면 끝까지 돌리고, 아니면 다시 i = 0으로 돌아가야해.
                i = 0
                prior_process = priorities[0]
            elif i == location:
                print(answer)
                quit()
        print(priorities, prior_process)
    return answer

priorities = [1,1,9,1,1,1] #[2,1,3,2]
location = 0 #2
print(solution(priorities, location))