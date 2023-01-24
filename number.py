import math

class Number:
    def __init__(self,num):
        self.number = num
    def data_type(self):
        """
        Number is type

        """
        return type(self.number)
    def data_len(self):
        """
        Number is len

        """
        if type(self.number)==float:
            return len(str(self.number))-1
        else:
            return len(str(self.number))
    def is_positive(self):
        """
        Number is positive

        """
        return (self.number)>0
    def is_nepositive(self):
        """
        Number is nepositive

        """
        return (self.number)<0
    def is_zero(self):
        """
        Number is zero

        """
        return (self.number)==0
    def is_even(self):
        """
        Number is even

        """
        return (self.number)%2==0
    def is_odd(self):
        """
        Number is odd

        """
        return (self.number)%2!=0
    def is_prime(self):
        """
        Number is positive

        """
        n=0
        for i in range(self.number):
            if self.number//i==0:
                n+=1
            
        return n==2


