import math

class Number:
    def __init__(self,num):
        self.number = num


    # Create methods of Number class


    def data_type(self)->type:
        """
        function that returns the type of the number

        """
        return type(self.number)


    def data_len(self)->len:
        """
        a function that returns the length of a number

        """
        if type(self.number)==float:
            return len(str(self.number))-1
        else:
            return len(str(self.number))


    def is_positive(self)->bool:
        """
        function that checks the positivity of a number

        """
        return (self.number)>0


    def is_nepositive(self)->bool:
        """
        function that checks the negativity of a number

        """
        return (self.number)<0


    def is_zero(self)->bool:
        """
        checking that the number is zero 

        """
        return (self.number)==0


    def is_even(self)->bool:
        """
        a function that determines the evenness of a number

        """
        return (self.number)%2==0


    def is_odd(self)->bool:
        """
        a function that determines the oddness of a number

        """
        return (self.number)%2!=0


    def is_prime(self):
        """
        a function that checks the integrity of a number

        """
        n=0
        for i in range(self.number):
            if self.number//i==0:
                n+=1
            
        return n==2
    