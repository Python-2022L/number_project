import math

class Number:
    def __init__(self,num):
        self.number = num

    def data_type(self):
        return type(self.number)
    
    def len(self):
        return len(self.number)
    
    def is_positive(self):
        return self.number > 0
    
    def is_negative(self):
        return self.number < 0
    
    def is_zero(self):
        return self.number == 0
    
    def is_even(self):
        return  self.number % 2 == 0
    
    def is_odd(self):
        return self.number % 2 != 0