class square:
    def __init__(self, variable, num = 0):
        self.variable = variable
        self.num = num

    def setNum(self, num):
        if num >= 1 and num <=9:
            self.num = num
            return True
        else:
            return False
        
    def getNum(self):
        return self.num

    def getType(self):
        return self.variable

    def setType(self, variable):
        if type(variable) == bool:
            self.variable = variable
            return True
        else:
            return False

    def __str__(self):
        return str(self.num)