from predict_table import PredictTable
from counter import Counter

class TwoBitBP():

    def __init__(self, table_size):
        self.table = PredictTable(table_size)

    def findCounter(self, address):
        counter = self.table.getEntry(address, Counter())

        return counter

    def predict(self, address):
        counter = self.findCounter(address)

        return counter.predict()
    
    def update(self, address, result):
        counter = self.findCounter(address)

        counter.update(result)
 
