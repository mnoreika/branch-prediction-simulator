from trace import Trace

class Simulator():

    def __init__(self, trace_file):
        self.traces = self.readTraceFile(trace_file)

    def readTraceFile(self, trace_file):
        with open(trace_file) as file:
            lines = file.readlines()

            traces = []
            for line in lines:
                line = line.split()
                traces.append(Trace(line[0], line[1]))
 
            return traces           

    def simulate(self, predictor): 
        miss_rate = 0

        for trace in self.traces:
            result = predictor.predict(trace.address)
        
            if (result != trace.taken):
                miss_rate += 1
        
            predictor.update(trace.address, trace.taken)
     
        return (miss_rate / len(self.traces)) * 100


