# Count the consonants in a string
def consonant_count(s):
    cons_set = {'H', 'K', 'm', 'L', 'k', 'd', 'V', 'S', 'n', 'l', 'h', 'p', 'q', 'j', 't', 'J', 'M', 'Z', 'x', 'Y', 'w', 'y', 'W', 'T', 'B', 'g', 'C', 'D', 'F', 's', 'r', 'X', 'R', 'N', 'f', 'z', 'G', 'v', 'Q', 'c', 'b', 'P'}
    count = 0
    for x in s:
        if x in cons_set:
            count += 1
    return count


