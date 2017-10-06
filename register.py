class Register():
    
    def __init__(self):
        self.history = []

    def put(self, value):
        self.history.append(value)

    def read(self):
        return self.history

    def readLast(self):
        return self.history[-1]
