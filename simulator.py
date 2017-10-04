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
    
    return miss_rate

def twoBitBP(traces):
    miss_rate = 0

    for trace in traces:
        #Predict and update counter
        if trace.counter[0] == 0:
            if trace.taken == 1:
                miss_rate += 1
                if trace.counter[1] == 0:
                    trace.counter[1] = 1
                else:
                    trace.counter[0] = 1;
                    trace.counter[1] = 0;
            else:
                trace.counter[1] = 0
        else:
            if trace.taken == 0:
                miss_rate += 1
                if trace.counter[1] == 0:
                    trace

                


    # Update counter


traces = readTraceFile()


