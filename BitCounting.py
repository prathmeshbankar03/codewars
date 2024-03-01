def count_bits(n):
    count = 0
    for i in str(bin(n)).split("0b")[1]:
        if i == '1':
            count+=1
    return count