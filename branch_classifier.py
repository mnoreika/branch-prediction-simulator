class BranchClassifier():
    
    def __init__(self):
        self.threshold = 60

    def generateProfile(self, traces, index_size):
        taken_count = {}
        ntaken_count = {}
        total_count = {}
        profile = {}

        for trace in traces:
            branch_index = trace.address[-index_size:]

            if branch_index not in taken_count:
                taken_count[branch_index] = 0
                ntaken_count[branch_index] = 0
                total_count[branch_index] = 0

            if trace.taken == 1:
                taken_count[branch_index] += 1
            else:
                ntaken_count[branch_index] += 1

            total_count [branch_index] += 1

        
        for branch in taken_count:
            taken_rate = taken_count[branch] / total_count[branch] * 100
            ntaken_rate = ntaken_count[branch] / total_count[branch] * 100
          
            # Classify as always taken
            if taken_rate >= self.threshold:
                profile[branch] = 1

            # Classify as never taken
            elif ntaken_rate >= self.threshold:
                profile[branch] = 0

            # Classify as hard to predict
            else:
                profile[branch] = 2


        return profile
