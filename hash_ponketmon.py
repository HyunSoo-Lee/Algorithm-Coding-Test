# 해시 > 폰켓몬
# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0
    get = len(nums)/2

    # 중복 제거 리스트
    nums_count = []
    for i in range(len(nums)):
        if nums[i] not in nums_count:
            nums_count.append(nums[i])
    cnt = len(nums_count)

    # 가져가야 하는 개수와 종류 수 비교
    if get >= cnt:
        answer = cnt
    else:
        answer = get

    return answer 

print(solution([3, 1, 2, 3]))