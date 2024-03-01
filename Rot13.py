def rot13(message):
    alp = "abcdefghijklmnopqrstuvwxyz"
    capalp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


    rot13 = ""
    for i in range(0,len(message)):
        if message[i].islower() == True:   
            num = alp.find(message[i])
            if num+13<26:
                rot13+=alp[num+13]
            else:
                rot13+=alp[num-26+13]

        elif message[i].isupper() == True:
            num = capalp.find(message[i])
            if num+13 < 26:
                rot13+=capalp[num+13]
            else:
                rot13+=capalp[num-26+13]

        elif message[i] == " ":
            rot13+=" "

        elif message[i].isdigit():
            rot13+=message[i]

        else:
            rot13+=message[i]
    return rot13