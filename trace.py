class Trace:

    def __init__(self, address, taken):
        self.address = address
        self.taken = int(taken)
        self.counter = [0, 0]
