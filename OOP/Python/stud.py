class Students:

    def __init__(self, fname, lname, dept): # constructor or class init
        """self: is used to refer to instance of the class.
        we use this by  convention as we donot know on which object we will apply"""
        self.fname = fname
        self.lname = lname
        self.dept = dept
    def setEmail(self): # it is instance method or behaviour or action
        return "{}{}{}".format(self.fname,".", self.lname) + "@" + "hu.edu.et"
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)
if __name__=="__main__":
    std1 = Students("Miki", "Yousuf", "Bioinformatics")
    print(std1.setEmail())
    print(std1.fullname())
