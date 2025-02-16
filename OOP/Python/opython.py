class Students:
    pass # writing a blueprint or template for objects
std1 = Students()
std2 = Students() # object instantiation

std1.fname = "Miki"
std1.lname = "Yousuf"
std1.dept = "Bioinformatics"
std2.fname = "Ayan"
std2.lname = "Abas"
std2.dept = "Enginering"

print(std1.fname, std1.lname)

