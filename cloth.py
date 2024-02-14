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
    
    print(codi)
    
    answer = 1
    return answer

solution(clothes)