def disemvowel(string_):
    empty_string=""
    for i in string_:
        if i in "aeiouAEIOU":
            empty_string+=''
        else:
            empty_string+=i
    return empty_string