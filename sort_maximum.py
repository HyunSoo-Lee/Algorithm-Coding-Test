# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    #answer = 0
    n = len(numbers)
    print(numbers)
    for i in range (n-1):
        for j in range(n-i-1):
            print('i = ' + str(i) + ' j = ' + str(j) + ' n = ' + str(n))
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                print(numbers)
    return numbers
    #return answer


numbers = [3,30,34,5,9]
print(solution(numbers))