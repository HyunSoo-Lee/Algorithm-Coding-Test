# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

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
    print(music_dict)
    
    return answer

print(solution(genres,plays))
