from predict_table import PredictTable
from counter import Counter

class TwoBitBP():

    def __init__(self, table_size):
        self.table = PredictTable(table_size)

    def predict(self, address):
        counter = self.table.getEntry(address, Counter())

        return counter.predict()
    
    def update(self, address, result):
        counter = self.table.getEntry(address, Counter())

        counter.update(result)
 
