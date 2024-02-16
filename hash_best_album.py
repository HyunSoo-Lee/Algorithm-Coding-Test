# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42579?language=python

genres = ["classic", "pop", "classic", "classic", "pop", "classic"]
plays = [500, 600, 150, 800, 2500, 800]

def solution(genres, plays):
    answer = []
    music_dict = {}
    # 장르 묶어서 딕셔너리 만들어주기
    for i in range(len(genres)):
        song = [plays[i],i]
        if genres[i] in music_dict:
            music_dict[genres[i]].append(song)
        else:
            music_dict[genres[i]] = [song]

    #장르 내 플레이 횟수 맞춰서 소팅해주기
    for genres, songs in music_dict.items():
        music_dict[genres] = sorted(songs, key=lambda x: x[0])
    print(music_dict)
    
    # while문 돌리면서 확인해야 하는것 : 
    # 가장 큰 값을 가진 장르에서 두개 빼오고 지우기 반복
    while music_dict:
        # print(music_dict)
        max_genre = max(music_dict, key = lambda x : x[-1][0])
        # print(max_genre)
        # print(music_dict[max_genre])
        # print(music_dict[max_genre][-1][0])
        if len(music_dict[max_genre]) > 2:
            if music_dict[max_genre][-1][0] == music_dict[max_genre][-2][0]:
                answer.append(music_dict[max_genre][-2][1])
                answer.append(music_dict[max_genre][-1][1])    
            else:
                answer.append(music_dict[max_genre][-1][1])
                answer.append(music_dict[max_genre][-2][1])
        elif len(music_dict[max_genre]) == 2:
            if music_dict[max_genre][1][0] == music_dict[max_genre][0][0]:
                answer.append(music_dict[max_genre][0][1])
                answer.append(music_dict[max_genre][1][1])
            else:
                answer.append(music_dict[max_genre][1][1])
                answer.append(music_dict[max_genre][0][1])
        elif len(music_dict[max_genre]) == 1:
            answer.append(music_dict[max_genre][0][1])
        del music_dict[max_genre]
    return answer

print(solution(genres,plays))
