# This code is not finished yet
x = ["Frici", "Beni", "1234", "Laci", "László", "Áron", "12345", "Dóri", "Péter", "123", "5"]
y = ["123", "Ryan", "Cool Man" "Jimmy", "4"]
def friend(x):
    for i in x:
        if len(i) != 4:
            x.remove(i)
    return(x)
friend(x)

x = ["Frici", "Beni", "1234", "Laci", "László", "Áron", "12345", "Dóri", "Péter"]
def friend(x):
    new_list = [i for i in x if len(i) == 4]
    return(new_list)
friend(x)