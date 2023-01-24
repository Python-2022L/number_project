import math

class Number:
    def __init__(self,num):
        self.number = num

    def len(self):
        return len(str(self.number))
x=Number(10)
print(x.len())