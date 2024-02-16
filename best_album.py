# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42579?language=python

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []
    music_dict = {}
    # O(n)
    for i in range(len(genres)):
        song = [plays[i],i]
        if genres[i] in music_dict:
            music_dict[genres[i]].append(song)
        else:
            music_dict[genres[i]] = [song]
    for genres, songs in music_dict.items():
        music_dict[genres] = sorted(songs, key=lambda x: x[0])
    for genres, songs in music_dict.items():
        if len(songs) == 2:
            print(songs)
        else:
            print(songs[1:])

    return answer

solution(genres,plays)
