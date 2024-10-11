# 해시 > 베스트 앨범
# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42579?language=python

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []
    g_dict = {}
    # zip함수는 여러 이터러블(리스트, 튜플 등)을 병렬로 묶어준다.
    # enumerate 함수는 이터러블을 입력받아, 해당 (인덱스,원소) 형태로 바꾸어준다.
    # 장르 : [[재생회수,고유번호], [재생회수,고유번호]...] 형태의 딕셔너리로 전환
    for i, (g, p) in enumerate(zip(genres,plays)):
            #print(f"인덱스 : {i}, 장르 : {g}, 횟수  : {p}")
            if g not in g_dict:
                  g_dict[g] = []
            g_dict[g].append([p,i])

    #print(g_dict)
    # 속한 노래가 많이 재생된 장르를 먼저 수록
    # 딕셔너리를 재생순으로 재정렬
    for key in g_dict:
        g_dict[key].sort(key=lambda x: x[0], reverse=True)
    #print(g_dict)
    #가장 큰 재생회수를 가진 장르 순으로 리스트
    g_sort = []
    p_max = 0
    for key in g_dict:
        if g_dict[key][0][0] > p_max:
            g_sort.append(key)
            p_max = g_dict[key][0][0]
    g_sort.reverse()
    #print(g_sort, p_max)
    # 장르 내에서 많이 재생된 노래를 먼저 수록
    for g in g_sort:
        answer.append(g_dict[g][0][1])
        answer.append(g_dict[g][1][1])
    # 장르 내에서 재생 횟수가 같은 노래중에서는 고유 번호가 낮은 노래를 먼저 수록
    return answer

print(solution(genres,plays))
