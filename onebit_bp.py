from predict_table import PredictTable

class OneBitBP():
    
    def __init__(self, table_size):
        self.table = PredictTable(table_size)

    def predict(self, address):
        counter_value = self.table.getEntry(address, 0)

        return counter_value
    
    def update(self, address, result):
        self.table.updateEntry(address, result)
 
