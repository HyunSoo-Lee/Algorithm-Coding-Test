# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# Test case 1
phone_book = ["119", "97674223", "1195524421"]
# Test case 2	
# phone_book = ["123","456","789"]
# Test case 3
# phone_book = ["12","123","1235","567","88"]


def solution(phone_book):
    answer = True
    dict_book = {i:phone_book[i] for i in range(len(phone_book))}
    print(dict_book)

    for i in range(len(phone_book)):
        print('i is ',i, phone_book[i])
        for j in range(len(phone_book)):
            if i == j:
                break
            if phone_book[i] in phone_book[j]:
                phone_book[j]
                print(phone_book[i])
                dict_book.pop(phone_book[j])
    print(dict_book)
    return answer

print(solution(phone_book))