import math
from trace import Trace
from counter import Counter

def readTraceFile():
    with open("branchtrace.out") as file:
        lines = file.readlines()

        traces = []
        for line in lines:
            line = line.split()
            traces.append(Trace(line[0], line[1]))
 
        return traces           

def alwaysBP(traces, prediction):
    miss_rate = 0

    for trace in traces:
        if trace.taken != prediction:
            miss_rate += 1
    
    return miss_rate

def twoBitBP(traces, table_size):
    miss_rate = 0
    predict_table = {}
    index_size = round(math.log2(table_size))
     
    for trace in traces:
        index = bin(int(trace.address))[-index_size:]
        print (index)
        
        if index not in predict_table:
            predict_table[index] = Counter()
        
        counter = predict_table[index]

        prediction = counter.predict()
        
        if (prediction != trace.taken):
            miss_rate += 1
        
        counter.update(trace.taken)

    return miss_rate

traces = readTraceFile()
    # Update counter

print(twoBitBP(traces, 512) / len(traces))

