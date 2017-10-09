import math
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

def xor(binaryA, binaryB):
    result = int(binaryA, 2) ^ int(binaryB, 2)
    return '{0:0{1}b}'.format(result, len(binaryA))

def simulate(predictor, traces): 
    miss_rate = 0

    for trace in traces:
        result = predictor.predict(trace.address)
        
        if (result != trace.taken):
            miss_rate += 1
        
        predictor.update(trace.address, trace.taken)
     
    return miss_rate

def gsharedBP(traces, table_size):
    miss_rate = 0
    predict_table = {}
    index_size = round(math.log2(table_size))
    register = Register(index_size)

    for trace in traces:
        address_bits = bin(int(trace.address))[-index_size:]
        index = xor(address_bits, register.read())
        
        if index not in predict_table:
            predict_table[index] = Counter()

        counter = predict_table[index]

        prediction = counter.predict()
    
        if (prediction != trace.taken):
            miss_rate += 1
        
        counter.update(trace.taken) 
        register.record(trace.taken)

    return miss_rate



traces = readTraceFile()
predictor3 = GShareBP(512, 9)
print (simulate(predictor3, traces)) 
print (gsharedBP(traces, 512))
