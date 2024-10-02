#2023 KAKAO BLIND RECRUITMENT, 개인정보 수집 유효기간

def comp_date(dp, dt, terms):
    arr_dp = (dp.split('.'))
    arr_dt = (dt.split('.'))
    for i in range (len(arr_dp)): arr_dp[i] = int(arr_dp[i])
    for i in range (len(arr_dt)): arr_dt[i] = int(arr_dt[i])
    
    arr_dp[1] += terms
    if arr_dp[1] > 12:
        y, arr_dp[1] = divmod(arr_dp[1],12)
        arr_dp[0] += y
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

print(solution("2020.04.16", ["A 36", "S 4"], ["2017.04.17 A", "2014.04.16 S"]))