import math
from predict_table import PredictTable
from register import Register
from counter import Counter

class GShareBP():

    def __init__(self, table_size, register_size):
        self.table = PredictTable(table_size)
        self.register = Register(register_size)  
        self.key_size = round(math.log2(table_size)) 

    def xor(self, binaryA, binaryB):
        result = int(binaryA, 2) ^ int(binaryB, 2)
        return '{0:0{1}b}'.format(result, len(binaryA))      

    def findCounter(self, address):
        index = self.xor(bin(int(address[:self.key_size])), self.register.read())
        
        print (address[:self.key_size])

        counter = self.table.getEntry(index, Counter())

        return counter

    def predict(self, address):
        counter = self.findCounter(address)
        
        return counter.predict()

    def update(self, address, result):
        counter = self.findCounter(address)

        counter.update(result)
        self.register.record(result)

