import math

class Calculator:
    
    def __init__(self):
        self.state = 0
        self.memory = 0
        self.display_mode = 'decimal'  # decimal, binary, octal, hexadecimal
        self.units_mode = 'degrees'  # degrees or radians
        self.error = False
    
    # ===== CORE FEATURES =====
    
    def get_display(self):
        """Get the current value on display"""
        if self.error:
            return "Err"
        return self.state
    
    def clear(self):
        """Clear the display"""
        self.state = 0
        self.error = False
    
    def add(self, x, y=None):
        """Add y to x, or add x to current state"""
        if y is None:
            self.state += x
        else:
            return x + y
        return self.state
    
    def subtract(self, x, y=None):
        """Subtract y from x, or subtract x from current state"""
        if y is None:
            self.state -= x
        else:
            return x - y
        return self.state
    
    def multiply(self, x, y=None):
        """Multiply x by y, or multiply state by x"""
        if y is None:
            self.state *= x
        else:
            return x * y
        return self.state
    
    def divide(self, x, y=None):
        """Divide x by y, or divide state by x"""
        if y is None:
            if x == 0:
                self.error = True
                self.state = "Err"
                return self.state
            self.state /= x
        else:
            if y == 0:
                self.error = True
                return "Err"
            return x / y
        return self.state
    
    def square(self):
        """Calculate x^2"""
        self.state = self.state ** 2
        return self.state
    
    def square_root(self):
        """Calculate √x"""
        if self.state < 0:
            self.error = True
            self.state = "Err"
            return self.state
        self.state = math.sqrt(self.state)
        return self.state
    
    def power(self, exponent):
        """Calculate x^y"""
        try:
            self.state = self.state ** exponent
        except:
            self.error = True
            self.state = "Err"
        return self.state
    
    def inverse(self):
        """Calculate 1/x"""
        if self.state == 0:
            self.error = True
            self.state = "Err"
            return self.state
        self.state = 1 / self.state
        return self.state
    
    def switch_sign(self):
        """Toggle sign: x to -x"""
        if not self.error:
            self.state = -self.state
        return self.state
    
    # ===== SCIENTIFIC FEATURES: TRIGONOMETRY =====
    
    def _convert_to_radians(self, value):
        """Convert value from current units mode to radians"""
        if self.units_mode == 'degrees':
            return math.radians(value)
        return value
    
    def _convert_from_radians(self, value):
        """Convert value from radians to current units mode"""
        if self.units_mode == 'degrees':
            return math.degrees(value)
        return value
    
    def sine(self):
        """Calculate sin(x)"""
        if self.error:
            return self.state
        rad = self._convert_to_radians(self.state)
        self.state = math.sin(rad)
        return self.state
    
    def cosine(self):
        """Calculate cos(x)"""
        if self.error:
            return self.state
        rad = self._convert_to_radians(self.state)
        self.state = math.cos(rad)
        return self.state
    
    def tangent(self):
        """Calculate tan(x)"""
        if self.error:
            return self.state
        rad = self._convert_to_radians(self.state)
        self.state = math.tan(rad)
        return self.state
    
    def inverse_sine(self):
        """Calculate arcsin(x)"""
        if self.error:
            return self.state
        if self.state < -1 or self.state > 1:
            self.error = True
            self.state = "Err"
            return self.state
        rad = math.asin(self.state)
        self.state = self._convert_from_radians(rad)
        return self.state
    
    def inverse_cosine(self):
        """Calculate arccos(x)"""
        if self.error:
            return self.state
        if self.state < -1 or self.state > 1:
            self.error = True
            self.state = "Err"
            return self.state
        rad = math.acos(self.state)
        self.state = self._convert_from_radians(rad)
        return self.state
    
    def inverse_tangent(self):
        """Calculate arctan(x)"""
        if self.error:
            return self.state
        rad = math.atan(self.state)
        self.state = self._convert_from_radians(rad)
        return self.state
    
    # ===== SCIENTIFIC FEATURES: DISPLAY MODES =====
    
    def switch_display_mode(self, mode=None):
        """Switch display mode or rotate through modes"""
        modes = ['decimal', 'binary', 'octal', 'hexadecimal']
        if mode is None:
            # Rotate to next mode
            current_idx = modes.index(self.display_mode)
            self.display_mode = modes[(current_idx + 1) % len(modes)]
        else:
            if mode.lower() in modes:
                self.display_mode = mode.lower()
        return self.display_mode
    
    def format_display(self):
        """Format the state according to current display mode"""
        if self.error:
            return "Err"
        
        value = int(self.state) if isinstance(self.state, (int, float)) else self.state
        
        if self.display_mode == 'binary':
            return bin(value)  # 0b...
        elif self.display_mode == 'octal':
            return oct(value)  # 0o...
        elif self.display_mode == 'hexadecimal':
            return hex(value)  # 0x...
        else:  # decimal
            return str(self.state)
    
    # ===== SCIENTIFIC FEATURES: MEMORY =====
    
    def memory_add(self):
        """M+ key: Add current display to memory"""
        if not self.error:
            self.memory += self.state
        return self.memory
    
    def memory_clear(self):
        """MC key: Clear memory"""
        self.memory = 0
        return self.memory
    
    def memory_recall(self):
        """MRC key: Recall memory to display"""
        if not self.error:
            self.state = self.memory
        return self.state
    
    # ===== SCIENTIFIC FEATURES: UNITS =====
    
    def switch_units_mode(self, mode=None):
        """Switch units mode (degrees/radians)"""
        modes = ['degrees', 'radians']
        if mode is None:
            # Rotate to next mode
            current_idx = modes.index(self.units_mode)
            self.units_mode = modes[(current_idx + 1) % len(modes)]
        else:
            if mode.lower() in modes:
                self.units_mode = mode.lower()
        return self.units_mode
    
    # ===== BONUS FEATURES =====
    
    def factorial(self):
        """Calculate x!"""
        if self.error:
            return self.state
        if self.state < 0 or self.state != int(self.state):
            self.error = True
            self.state = "Err"
            return self.state
        self.state = math.factorial(int(self.state))
        return self.state
    
    def logarithm(self, base=10):
        """Calculate log base b of x"""
        if self.error:
            return self.state
        if self.state <= 0:
            self.error = True
            self.state = "Err"
            return self.state
        self.state = math.log(self.state, base)
        return self.state
    
    def natural_logarithm(self):
        """Calculate ln(x)"""
        if self.error:
            return self.state
        if self.state <= 0:
            self.error = True
            self.state = "Err"
            return self.state
        self.state = math.log(self.state)
        return self.state
    
    def inverse_log(self, base=10):
        """Calculate b^x (inverse logarithm)"""
        if self.error:
            return self.state
        self.state = base ** self.state
        return self.state
    
    def inverse_natural_log(self):
        """Calculate e^x (inverse natural logarithm)"""
        if self.error:
            return self.state
        self.state = math.e ** self.state
        return self.state
    
    # ===== CUSTOM FEATURES =====
    
    def percentage(self):
        """Convert current value to percentage (divide by 100)"""
        if not self.error:
            self.state = self.state / 100
        return self.state
    
    def absolute_value(self):
        """Get absolute value of current state"""
        if not self.error:
            self.state = abs(self.state)
        return self.state