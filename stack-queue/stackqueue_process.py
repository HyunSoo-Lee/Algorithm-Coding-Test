# 스택/큐 > 프로세스
# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    order = []
    pointer = 0
    while True:
        if max(priorities) == 0:
            break
        else: 
            print(pointer, len(priorities),priorities[pointer])
            if priorities[pointer] == max(priorities):
                priorities[pointer] = 0
                order.append(pointer)
                print(priorities)
            if pointer == len(priorities) - 1:
                pointer = 0
            else: pointer += 1
    print(order)
    answer = order.index(location) + 1
    return answer

priorities = [1, 1, 9, 1, 1, 1]	
location = 0
print(solution(priorities, location))