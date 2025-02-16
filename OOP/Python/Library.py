#class Libraries:
 #   pass
#book1 = Libraries() # first instances
#book2 = Libraries() # second instances

#print(book1)
#print(book2)

#book1.name = "Geography"
#book1.year = 1999 # instance attributes
#book1.shelf = "Fourth"
#book1.volume = 3
#book1.status = "Taken"

#print(book1.name)

### Doing all these manually is tedious

class Libraries:
    def __init__(self, name, year, shelf, volume):
        self.name = name
        self.year = year
        self.shelf = shelf
        self.volume = volume
    def status(self):
        if self.year < 2000:
            print("Look at OLD")
        else:
            print("Not Available")
    
book1 = Libraries("Geography", 2024, "Five", 3)
book1.status()
print(book1.year)
