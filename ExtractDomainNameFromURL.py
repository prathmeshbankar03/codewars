def domain_name(url):
    try:
        if "https://" or "http://" in url:
            if "www." in url.split("/")[2]:
                return url.split("/")[2].split(".")[1]
            else:
                return url.split("/")[2].split(".")[0]
    except:
        if "www." in url:
            return url.split(".")[1]
        else:
            return url.split(".")[0]