class Number:
    def __init__(self,num):
        self.number = num
    
    def len(self):
        return len(str(self.number))
    
    def data_type(self):
        return type(self.number())

    def is_positive(self):
        return self.number > 0
    
    def is_negative(self):
        return self.number < 0
    
    def is_zero(self):
        return self.number == 0
    
    def is_even(self):
        return self.number%2 == 0
    
    def is_odd(self):
        return self.number%2 == 1

    def is_prime(self):
        k=0
        for i in range(1,self.number+1):
            if self.number%i == 0:
                k+=1
        if k==2 or k==1:
            return True
        else:
            return False      

x=Number(10)
print(x.is_prime())