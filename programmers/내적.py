def solution(a, b):
    answer = 0
    for x in zip(a, b):
        answer += x[0]*x[1]
    return answer