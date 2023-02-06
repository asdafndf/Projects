# Abc, vowels, consonants
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ

letters_list = list(string.ascii_lowercase)
number_list = range(1, 27, 1)

letter_number = zip(letters_list, number_list)

alphabet_with_position = {char:number for char, number in letter_number}

vowel = "aeiouAEIOU"
consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

