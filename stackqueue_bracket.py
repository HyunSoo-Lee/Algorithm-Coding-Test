# 스택/큐 > 올바른 괄호
# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stk = []
    for i in range(len(s)):
        if s[i] == '(':
            stk.append(s[i])
        else:
            if stk:
                stk.pop()
            else:
                return False
    if len(stk) == 0:
        return True
    else:
        return False  # 명시적으로 False를 반환


print(solution(""))