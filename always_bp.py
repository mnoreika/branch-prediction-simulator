class AlwaysBP():

    def __init__(self, mode):
        self.mode = mode

    def predict(self, address):
        return self.mode
    
    def update(self, address, taken):
        pass
        
