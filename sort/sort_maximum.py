# 정렬 > 가장 큰 수
# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42746
def comp(x, y):
    # print(int(str(x) + str(y)))
    # print(int(str(y) + str(x)))
    if (int(str(x) + str(y)) > int(str(y) + str(x))):
        return False
    else:
        return True


def solution(numbers): 
    #answer = 0
    n = len(numbers)
    #print(numbers)
    for i in range (n-1):
        swapped = False
        for j in range(n-i-1):
            #print('비교 대상',numbers[j],numbers[j+1])
            #if numbers[j] > numbers[j+1] and comp(numbers[j], numbers[j+1]):
            if comp(numbers[j], numbers[j+1]):
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                #print(numbers)
                swapped = True
        if not swapped:
            break
    numbers = [str(n) for n in numbers]
    result = ''.join(numbers)
    return result if result[0] != '0' else '0'
    #return answer

#and comp(numbers[j], numbers[j+1])

numbers = [3,30,34,5,9]
#numbers = [6, 10, 2]
print(solution(numbers))

