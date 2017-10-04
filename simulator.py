from trace import Trace

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
    
    return miss_rate / len(traces)


traces = readTraceFile()
    
print("Always not taken:", alwaysBP(traces, '0'))
print("Always taken:", alwaysBP(traces, '1'))

