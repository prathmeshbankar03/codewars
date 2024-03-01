def solution(s):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    str = ""

    for i in s:
        if i in alpha:
            str+=" "+i
        else:
            str+=i
    return str
