def generate_hashtag(s):
    if len(s)==0 or len(s)>140:  
        return False
    else:
        str = ""
        for i in s.split(" "):
            str+=i.capitalize()
        return "#"+str