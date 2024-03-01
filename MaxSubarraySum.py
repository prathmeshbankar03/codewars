def max_sequence(arr):
    max = 0
    sum = 0
    for i in range(0,len(arr)):
        sum+= arr[i]
        if sum > max:
            max = sum
        if sum < 0:
            sum = 0
    return max
