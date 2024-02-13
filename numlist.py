# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# Test case 1
phone_book = ["97674223119", "119", "1195524421"]
# Test case 2	
# phone_book = ["123","456","789"]
# Test case 3
# phone_book = ["12","123","1235","567","88"]


# 리스트 컴프리헨션을 두번 돌리는 경우
# -> 포함 여부로 for문 한번 돌리면서 컴프리핸션
# -> 포함된 리스트 따로 뽑아서 맨 앞에 포함이 되어있는지 확인...?

def solution(phone_book):
    answer = True
    # 정석적인 풀이법
    # for i in range(len(phone_book)):
    #     # list comprehension
    #     include_num = [v for v in phone_book if phone_book[i] in v and phone_book[i] != v]
    #     if len(include_num) != 0:
    #         # print(phone_book[i], include_num)
    #         # include num 돌면서 포함된 문자열이 맨 앞에 있는지 확인
    #         for n in range(len(include_num)):
    #             if phone_book[i] == include_num[n][:len(phone_book[i])]:
    #                 # print(include_num[n], 'correct')
    #                 answer = False

    # 꼼수 풀이법
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])] and phone_book[i] != phone_book[j]:
                answer = False

    return answer

print(solution(phone_book))