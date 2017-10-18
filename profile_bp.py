import math
from branch_classifier import BranchClassifier
from gshare_bp import GShareBP

class ProfileBP():

    def __init__(self, table_size, register_size, traces):
        self.index_size = round(math.log2(table_size))
        self.classifier = BranchClassifier()
        self.profile = self.classifier.generateProfile(traces, self.index_size)
        self.gshare_predictor = GShareBP(table_size, register_size)

    def predict(self, address):
        if self.profile[address[-self.index_size:]] == 2:
            return self.gshare_predictor.predict(address)
        else:
            return self.profile[address[-self.index_size:]]

    
    def update(self, address, result):
        self.gshare_predictor.update(address, result)
 
