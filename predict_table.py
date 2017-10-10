import math

class PredictTable():

    def __init__(self, size):
        self.size = size
        self.table = {}
        self.key_size = round(math.log2(self.size)) 

    def produceKey(self, address):
        key = bin(int(address))[-self.key_size:]
        
        return key

    def getEntry(self, address, default_entry):
        key = self.produceKey(address)

        if key not in self.table:
           self.table[key] = default_entry

        return self.table[key]
    
    def updateEntry(self, address, result):
        key = self.produceKey(address) 

        self.table[key] = result
         
