class Bunny:
    def move(self):
        return "Hop!"
    
class Snake:
    def move(self):
        return "crawl!"
    
    
#  Polymorphism in action 
for animal in (Bunny(), Snake()):
    print(animal.move())      