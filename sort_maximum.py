# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42746
def comp(x, y):
    if (int(x + y) > int(y + x)):
        return True
    else:
        return False


def solution(numbers):
    
    #answer = 0
    n = len(numbers)
    print(numbers)
    for i in range (n-1):
        for j in range(n-i-1):
            print('비교 대상',numbers[j],numbers[j+1])
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                print(numbers)
    
    numbers = [str(n) for n in numbers]
    result = ''.join(reversed(numbers))
    return result
    #return answer

#and comp(numbers[j], numbers[j+1])

#numbers = [3,30,34,5,9]
numbers = [6, 10, 2]
print(solution(numbers))