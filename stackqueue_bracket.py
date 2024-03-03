# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    if '(' not in s:
        return False
    stk = []
    for i in range (len(s)):
        if s[i] == '(':
            stk.append(s[i])
        else:
            if stk:
                stk.pop()
    if len(stk) == 0:
        return True
    else:
        return False

print(solution(""))