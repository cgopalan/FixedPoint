class AFixedPoint:
    """
    Creates a Fixed Point object from a float or hex encoded value.
    """
    def __init__(self, fixedPoint):
        if type(fixedPoint) is float:
            floatAsStr = str(fixedPoint)
            self.signed = floatAsStr.startswith("-")
            self.integerPart, self.fractionalPart = map(int,
                    floatAsStr[1:].split(".") if self.signed 
                    else floatAsStr.split("."))
        elif str(fixedPoint).startswith("0x"):
            fpAsDec = int(str(fixedPoint), 16) 
            #Remove the '0b' and pad to 32 bits 
            fpAsBinStr = bin(fpAsDec)[2:].rjust(32, '0')
            #Extract first bit, which is sign, and then next 16 and then 15.
            self.signed =  fpAsBinStr.startswith("1")
            self.integerPart = int(fpAsBinStr[1:17], 2)
            self.fractionalPart = str(round(float(int(fpAsBinStr[17:], 2)) / (2**15), 2))[2:]
        else:
            print "Value supplied is not in hex format or float"
            
    def __str__(self):
        """
        Returns a string representation of the fixed point enclosed.
        """
        return '{0}{1}.{2}'.format("-" if self.signed else "",
                                    self.integerPart, self.fractionalPart)
                                    
    def __float__(self):
        """
        Returns the closest float value to the fixed point enclosed.
        """
        return float(("-" if self.signed else "") + str(self.integerPart) + 
                                "." + str(self.fractionalPart))