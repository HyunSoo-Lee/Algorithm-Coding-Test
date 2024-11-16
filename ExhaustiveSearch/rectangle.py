# 완전탐색 > 최소직사각형
# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/86491


def solution(sizes):
    answer = 0
    test = [60,50]
    for i in range(len(sizes)):
        #그냥 들어가는 케이스
        print(test, sizes[i])
        if test[0] >= sizes[i][0] and test[1] >= sizes[i][1]:
            continue
        else:
            #뒤집어서 들어가면 굳
            if test[0] >= sizes[i][1] and test[1] >= sizes[i][0]:
                continue
            #안들어가면...?
            else:
                #최소한으로 크기 늘리는법
                delta_1_w = test[0] - sizes[i][0]
                delta_1_h = test[1] - sizes[i][1]
                delta_1_s = 0
                #1번 세로가 모자란 경우
                if delta_1_w > 0 and delta_1_h < 0:
                    delta_1_s = abs(delta_1_h)
                elif delta_1_w < 0 and delta_1_h > 0:
                    delta_1_s = abs(delta_1_w)
                elif delta_1_w < 0 and delta_1_h < 0:
                    delta_1_s = abs(delta_1_w + delta_1_h)
                
                delta_2_w = test[0] - sizes[i][1]
                delta_2_h = test[1] - sizes[i][0]
                delta_2_s = 0
                #1번 세로가 모자란 경우
                if delta_2_w > 0 and delta_2_h < 0:
                    delta_2_s = abs(delta_2_h)
                elif delta_2_w < 0 and delta_2_h > 0:
                    delta_2_s = abs(delta_2_w)
                elif delta_2_w < 0 and delta_2_h < 0:
                    delta_2_s = abs(delta_2_w + delta_2_h)

                print(delta_1_s, delta_2_s)
                if delta_1_s > delta_2_s:
                    
                    test[0] += delta_2_w
                    test[1] += delta_2_h
                else:
                    test[0] += sizes[i][0]
                    test[1] += sizes[i][1]
    return answer


sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))