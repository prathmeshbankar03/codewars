def alphabet_position(text):
    nstr=""
    alp="abcdefghijklmnopqrstuvwxyz"
    for i in text.lower():
        if i in alp:
            nstr+=str(alp.find(i)+1)+" "
    return nstr[0:len(nstr)-1]