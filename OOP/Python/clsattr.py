class Students:

    courses = ["Python", "Project", "LA", "Calculus", "Biology"]
    NoStudents = []
    def __init__(self, fname, lname, dept):
        """"""
        self.fname = fname
        self.lname = lname
        self.dept = dept
        self.compulsory = ["Project", "Python"]
        Students.NoStudents.append(self)
    def fullname(self):
        return f"{self.fname} {self.lname}"
    def setEmail(self):
        return "{}{}{}".format(self.fname, ".", self.lname) + "@"+"hu.edu.et"
    def takenCourse(self, *crs):
        for c in crs:
            if c not in Students.courses:
                print(f"{c}", "Not Available")
            elif c in Students.courses and c not in self.compulsory:
                self.compulsory.append(c)
    @classmethod
    def regSub(cls):
        ## To findout the subjects where students are not registered in it
        pass
    @staticmethod
    def stat():
        pass
if __name__ == "__main__":
    std = Students("Michael", "Yousuf", "Bioinformatics")
    print(std.fullname())
    print(std.setEmail())
    std.takenCourse("Math", "Python", "Biology")
    print(std.compulsory)
