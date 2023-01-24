import math

class Number:
    def __init__(self,num):
        self.number = num

    def is_positive(self):
        return self.number>0



    

x = Number(10)

print(x.is_positive())

