class BMI:

    def __init__(self, weight:float, height:float, name:str, age:int):
        """
        """
        self.__weight = weight
        self.__height = height
        self.__name = name
        self.__age = age
    def getBMI(self):
        """
        """
        return self.__weight/(self.__height*self.__height)
    def getAge(self):
        """
        """
        return self.__age
    def getName(self):
        return self.__name
if __name__ == "__main__":
    bmi = BMI(90.0, 1.30, "miki", 34)
    print(bmi.getBMI())
