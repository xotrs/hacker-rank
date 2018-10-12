def minion_game(string):
    stuart_score = 0
    kevin_score = 0

    for i in range(len(string)):
        if string[i] in 'AEOUI':
            kevin_score += (len(string) - i)
        else:
            stuart_score += (len(string) - i)

    if kevin_score > stuart_score:
        return "Kevin "+str(kevin_score)
    elif kevin_score < stuart_score:
        return "Stuart "+str(stuart_score)
    else:
        return "Draw"


if __name__ == '__main__':
    s = input()
    minion_game(s)