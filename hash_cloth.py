# 해시 > 의상
# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

clothes = [
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"]
    ]

# 키 - 밸류

def solution(clothes):
    codi = {}

    # 주어진 리스트 순회
    for item in clothes:
        clothing_item, category = item
        # 해당 카테고리가 이미 딕셔너리에 존재한다면, 의상을 추가
        if category in codi:
            codi[category].append(clothing_item)
        # 카테고리 추가, 의상 추가
        else:
            codi[category] = [clothing_item]
    

    # 한가지인 경우 : a -> (a+1) - 1
    # 두가지인 경우 : a + b + ab -> (a+1)(b+1) - 1
    # 세가지인 경우 : a + b + ab + c + bc + ac + abc -> (a+1)(b+1)(c+1) - 1
    num = []
    for c, i in codi.items():
        num.append(len(i))
    answer = 1
    for i in range(len(num)):
        answer *= (num[i]+1)
    answer -= 1
    return answer

print(solution(clothes))