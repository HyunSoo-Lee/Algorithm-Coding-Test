# 해시 > 베스트 앨범
# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42579?language=python

genres = ["classic", "pop", "classic", "classic", "pop", "classic"]
plays = [500, 600, 150, 800, 2500, 800]

def solution(genres, plays):
    answer = []

    dict_genres = {}
    i = 0
    for k in genres:
        if k in dict_genres:
            dict_genres[k].append(plays[i])
        else:
            dict_genres[k] = [plays[i]]
        i += 1
    print(dict_genres)

    # 속한 노래가 많이 재생된 장르를 먼저 수록
    print(dict_genres.items())
    list_dict = list(dict_genres.items())
    print(list_dict)
    for k,v in list_dict:
        print(max(v))

    # 장르 내에서 많이 재생된 노래를 먼저 수록
    # 장르 내에서 재생 횟수가 같은 노래중에서는 고유 번호가 낮은 노래를 먼저 수록
    return answer

print(solution(genres,plays))
