def rgb(r,g,b):

    #red part
    if r > 255:
        r = 255
    if r < 0:
        r = 0
    if r < 10 :
        red = "0"+str(hex(r)).split('0x')[1]
    else:
        red = "".join(str(hex(r)).split('0x')[1])

    #green part
    if g > 255:
        g = 255
    if g < 0:
        g = 0
    if g < 10 :
        green = "0"+str(hex(g)).split('0x')[1]
    else:
        green = "".join(str(hex(g)).split('0x')[1])

    #blue part
    if b > 255:
        b = 255
    if b < 0:
        b = 0

    if b < 10 :
        blue = "0"+str(hex(b)).split('0x')[1]
    else:
        blue = "".join(str(hex(b)).split('0x')[1])

    return (red+green+blue).upper()

print(rgb(-20,275,125))