from predict_table import PredictTable
from register import Register
from counter_pool import CounterPool

class CorrelatingBP():

    def __init__(self, table_size, register_size):
        self.table = PredictTable(table_size)
        self.register = Register(register_size)
    
    def findCounter(self, address):
        counter_pool = self.table.getEntry(address, CounterPool())
        register_index = self.register.read()

        counter = counter_pool.getCounter(register_index)

        return counter

    def predict(self, address):
        counter = self.findCounter(address)

        return counter.predict()
    
    def update(self, address, taken):
        counter = self.findCounter(address)

        counter.update(taken)
        self.register.record(taken)        
        

 
