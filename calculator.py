import math // the math module provides access to mathematical functions

class calculator
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
        return self.display