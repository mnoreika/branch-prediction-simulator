class Counter:

    def __init__(self):
        self.count = [0, 0]
    
    def predict(self):
        if self.count[0] == 0:
            return 0;
        else:
            return 1;

    def update(self, taken):
        if self.count[0] == 0:
            if taken == 1:
                if self.count[1] == 0:
                    self.count[1] = 1
                else:
                    self.count[0] = 1
                    self.count[1] = 0
            else:
                self.count[1] = 0
        else:
            if taken == 0:
                if self.count[1] == 0:
                    self.count[0] = 0
                    self.count[1] = 1
                else:
                    self.count[1] = 0
            else:
                self.count[1] = 1

