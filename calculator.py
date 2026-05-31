import math # the math module provides access to mathematical functions

class Calculator:
    def __init__(self):
        self.state = 0
        self.error = False
        self.memory = 0
        self.display = 0
        
    def clear(self):
        self.state = 0
        self.error = False
        self.display = 0

    def get_display(self):
        if self.error:
            return "Error"
        return self.display
    
    def add(self, a, b= None):
        if self.error:
            return "Error"
        if b is None:
            self.display = a + self.state
        else:
            self.display = a + b
            self.state = self.display  
        return self.display
    
    def subtract(self, a, b= None):
        if self.error:
            return "Error"
        if b is None:
            self.display = self.state -a
        else:
            self.display = a - b
            self.state = self.display  
        return self.display
        
    def multiply(self, a, b=None):
        if self.error:
            return "Error"
        if b is None:
            self.display = a * self.state
        else: 
            self.display = a * b
            self.state = self.display
        return self.display
        
    def divide(self, a, b=None):
        if self.error:
            return "Error"
        if b is None:
            if a == 0:
             self.error = True
             return "Error"
            self.display = self.state / a
        else:
                    if b == 0:
                     self.error = True
                    return "Error"
        self.display = a / b
        self.state = self.display
        return self.display

    def power(self, a, b= None):
        if self.error:
            return "Error"
        if b is None:
            self.display = a ** self.state
        else:
            self.display = a ** b
        self.state = self.display
        return self.display

    def sqrt(self, a):
        if self.error:
            return "Error"
        if a<0:
            self.error = True
            return "Error"
        self.display = math.sqrt(a)
        self.state = self.display
        return self.display
    
    def sin(self, a, degrees=False):
        if self.error:
            return "Error"
        if degrees: 
            a = math.radians(a)
        self.display = math.sin(a)
        self.state = self.display
        return self.display
    
    def cosine(self, a, degrees=False):
        if self.error:
            return "Error"
        if degrees:
            a = math.radians(a)
            self.display = math.cos(a)
        return self.display
    
    def tangent(self, a, degrees = False):
        if self.error:
            return "Error"
        if degrees:
            a = math.radians(a)
        self.display = math.tan(a)
        self.state = self.display
        return self.display

    def log(self, a):
        if self.error:
            return "Error"
        if a <= 0:
            self.error = True
            return "Error"
        self.display = math.log10(a)
        self.state = self.display

        return self.display 
    
    def ln(self, a):
        if self.error:
            return "Error"
        if a <= 0:
            self.error = True
            return "Error"
        self.display = math.log(a)
        self.state = self.display
        return self.display
    
if __name__ == '__main__':
        calc = Calculator()
        print(calc.add(2,3))
        print(calc.subtract(10,4))
        print(calc.multiply(2,3))
        print(calc.divide(30,5))
        print(calc.sqrt(16))
        print(calc.power(2,3))
        print(calc.sin(90, degrees= True))
        print(calc.cosine(0, degrees= True))
        print(calc.tangent(45, degrees= True))
        print(calc.log(100))
        print(calc.ln(math.e))