def solution(board, moves):
    answer=0
    board_T = [list(x) for x in zip(*board)]
    board_new = []
    basket = [0]
    for i in range(len(board_T)):
        board_new.append(list(reversed(list(filter(lambda a: a!=0, board_T[i])))))

    for i in moves:
        try:
            tmp = board_new[i-1].pop()
            print(i, tmp, basket[-1])
            if basket[-1] == tmp:
                basket.pop()
                answer+=2
            else:
                basket.append(tmp)
        except:
            continue
    return answer