#2023 KAKAO BLIND RECRUITMENT, 개인정보 수집 유효기간

def comp_date(dp, dt, terms):
    arr_dp = (dp.split('.'))
    arr_dt = (dt.split('.'))
    for i in range (len(arr_dp)): arr_dp[i] = int(arr_dp[i])
    for i in range (len(arr_dt)): arr_dt[i] = int(arr_dt[i])
    
    #중요! 날짜 만드는 부분!
    new_month = arr_dp[1] + terms
    arr_dp[0] = (arr_dp[0]) + (new_month - 1) // 12
    arr_dp[1] = (new_month - 1) % 12 + 1
    print(arr_dp, arr_dt)
    
    if arr_dp[0] > arr_dt[0]:
        return False
    elif arr_dp[0] < arr_dt[0]:
        return True
    elif arr_dp[0] == arr_dt[0]:
        if arr_dp[1] > arr_dt[1]:
            return False
        elif arr_dp[1] < arr_dt[1]:
            return True
        elif arr_dp[1] == arr_dt[1]:
            if arr_dp[2] <= arr_dt[2]:
                return True
            else: return False

def solution(today, terms, privacies):
    answer = []
    dict_t = []
    dict_p =[]

    for i in range(len(terms)):
        dict_t.append([terms[i][0], terms[i][2:]])
    for i in range(len(privacies)):
        dict_p.append([privacies[i][:10], privacies[i][-1]])

    for i in range(len(dict_p)):
        for j in range(len(dict_t)):
            if dict_p[i][1] == dict_t[j][0]:
                if comp_date(dict_p[i][0], today, int(dict_t[j][1])):
                    answer.append(i+1)

    return answer



today = '2022.05.19'
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today, terms, privacies))

print(solution(	"2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))

print(solution("2020.10.01", ["A 11"], ["2019.12.01 A", "2000.01.01 A"]))