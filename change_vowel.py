# Solutions to the "Disemvowel Trolls" kata at codewars.com

def disemvowel(string_):
    result = ""
    for x in string_:
        if x.lower() not in "aeiou":
            result += x
    return result

def disemvowel(string_):
    for x in string_:
        if x.lower() in "aeiou":
            string_ = string_.replace(x, "")
    return string_

def disemvowel(string_):
    return "".join(x for x in string_ if x not in "aeiouAEIOU")

def disemvowel(string_):
    rules = {
        65 : None,
        69 : None,
        73 : None,
        79 : None,
        85 : None,
        97 : None,
        101 : None,
        105 : None,
        111 : None,
        117 : None
    }
    return string_.translate(rules)