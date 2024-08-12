# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    #answer = 0
    n = len(numbers)
    print(numbers)
    for i in range (n):
        for j in range(n - i - 1):
            print(i, j, n)
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                print(numbers)
    return numbers
    #return answer


numbers = [6,10,2]
print(solution(numbers))