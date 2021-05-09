def solution(array, commands):
    answer = []
    for idx in range(len(commands)):
        i, j, k = commands[idx]
        tmp = sorted(array[i-1:j])
        answer.append(tmp[k-1])
    return answer