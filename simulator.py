import sys
from trace import Trace
from counter import Counter
from register import Register
from counter_pool import CounterPool
from always_bp import AlwaysBP
from twobit_bp import TwoBitBP
from correlating_bp import CorrelatingBP
from gshare_bp import GShareBP

def readTraceFile():
    with open("branchtrace.out") as file:
        lines = file.readlines()

        traces = []
        for line in lines:
            line = line.split()
            traces.append(Trace(line[0], line[1]))
 
        return traces           

def simulate(predictor, traces): 
    miss_rate = 0

    for trace in traces:
        result = predictor.predict(trace.address)
        
        if (result != trace.taken):
            miss_rate += 1
        
        predictor.update(trace.address, trace.taken)
     
    return (miss_rate / len(traces)) * 100


traces = readTraceFile()

# Default values
table_size = 512
register_size = 9

if (len(sys.argv) > 1): 
    table_size = int(sys.argv[1])

if (len(sys.argv) > 2):
    register_size = int(sys.argv[2])

# Simulate branch predictors
predictor = AlwaysBP(1)
always_taken_result = simulate(predictor, traces)

predictor = AlwaysBP(0)
always_ntaken_result = simulate(predictor, traces)

predictor = TwoBitBP(table_size)
two_bit_result = simulate(predictor, traces)

predictor = CorrelatingBP(table_size, register_size)
correlated_result = simulate(predictor, traces)

predictor = GShareBP(table_size, register_size)
gshare_result = simulate(predictor, traces)


print ("AlwaysTaken: ", always_taken_result) 
print ("AlwaysNotTaken: ", always_ntaken_result)
print ("TwoBit: ", two_bit_result)
print ("Correlated: ", correlated_result)
print ("GShared: ", gshare_result)


