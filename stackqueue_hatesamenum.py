arr = [1,1,3,3,0,1,1]

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if not answer:
            answer.append(arr[i])
        elif answer[-1] != arr[i]:
            answer.append(arr[i])

    return answer

print(solution(arr))
