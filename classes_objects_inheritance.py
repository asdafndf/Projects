# Classes and objects, just a note to myself

class TV:
    def __init__(self, brand, colour, size, is_good):
        self.brand = brand
        self.colour = colour
        self.size = size
        self.is_good = is_good
    def is_it_big(self):
        return self.size >= 4
    def is_it_good(self):
        return self.is_good
    
TV_1 = TV("Samsung", "black", 5, True)
TV_2 = TV("LG", "brown", 4, False)
TV_3 = TV("Sony", "white", 3, False)

print(TV_1.brand)
print(TV_2.is_it_big())
print(TV_3.is_it_good())
TV.is_it_good(TV_3)

#Inheritance:
class Newspaper:
    def news(self):
        print("You can get the latest news")
    def entertain(self):
        print("You can entertain yourself")
    def sports(self):
        print("You can READ about sports")

class Television(Newspaper):
    def YT(self):
        print("You can watch YouTube")
    def sports(self):
        print("You can WATCH about sports")

paper = Newspaper()
paper.news()

tv = Television()
tv.YT()

tv.entertain()
tv.sports()


