# Defining a class
class book:
    color="Blue"

# Method
def __init__(self, title, author, ): 
    self.title=title
    self.author=author
    print("Holy Book")

# Creating an object
my_book=book()
print(my_book.color)

# Add an inheritance layer to explore polymorphism or encapsulation.
class book:
    def __init__(self, title, author): 
        self.title=title
        self.author=author
        
book=book("Corinthians", "Paul")
print(book.title)
print(book.author)

        
        




   