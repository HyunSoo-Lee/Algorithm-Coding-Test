# 정렬 > K번째 수
# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42748

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        arr = sorted(array[commands[i][0]-1:commands[i][1]])
        #print(arr[commands[i][2]-1])
        answer.append(arr[commands[i][2]-1])
    return answer

print(solution(array, commands))
