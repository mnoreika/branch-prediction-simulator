class Register():
    
    def __init__(self, size):
        self.history = ['0' for x in range(size)]

    def record(self, value):
        self.history = self.history[1:]
        self.history.append(str(value))

    def read(self):
        return ''.join(self.history)
