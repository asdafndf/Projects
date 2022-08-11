# Solutions to the "Disemvowel Trolls" kata at codewars.com

def disemvowel(string_):
    result = ""
    for x in string_:
        if x.lower() in "aeiou":
            continue
        else:
            result = result + x
    return result

def disemvowel(string_):
    for x in string_:
        if x.lower() in "aeiou":
            string_ = string_.replace(x, "")
    return string_