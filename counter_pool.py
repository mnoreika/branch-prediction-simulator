from counter import Counter
from collections import defaultdict

class CounterPool():
    
    def __init__(self):
        self.pool = defaultdict(lambda: Counter())
        
    def getCounter(self, index):
        return self.pool[index]

