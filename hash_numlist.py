# 해시 > 전화버노 목록
# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# Test case 1
phone_book = ["97674223", "119", "1195524421"]
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

    # for문을 줄이기 위해 list [:]를 사용해서 풀이
    # for i in range(len(phone_book)):
    #     for j in range(len(phone_book)):
    #         if phone_book[i] == phone_book[j][:len(phone_book[i])] and phone_book[i] != phone_book[j]:
    #             answer = False

    # 효율성 테스트 결과 O(n^2)은 무조건 탈락인듯. 다른 방법을 찾아야 한다.
    # list 내의 원소가 String 형태의 숫자들로 이루어진 경우,
    # 해당 숫자의 크기와 상관없이 첫째자리 숫자의 크기로 순서가 정해진다.
    phone_book.sort()
    #print(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])] : 
            answer = False
    return answer

print(solution(phone_book))