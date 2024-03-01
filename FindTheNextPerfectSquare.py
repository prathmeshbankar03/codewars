def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    sqrt=int(sq**0.5)
    if sqrt*sqrt == sq:
        return (sqrt+1)**2
    else:
        return -1
