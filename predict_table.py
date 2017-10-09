import math

class PredictTable():

    def __init__(self, size):
        self.size = size
        self.table = {}
        self.key_size = round(math.log2(self.size)) 

    def getEntry(self, address, default_entry):
        key = bin(int(address))[-self.key_size:]

        if key not in self.table:
           self.table[key] = default_entry

        return self.table[key]
    
        
