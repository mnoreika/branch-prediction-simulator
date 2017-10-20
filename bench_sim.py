import os
import csv
from simulator import Simulator
from always_bp import AlwaysBP
from onebit_bp import OneBitBP
from twobit_bp import TwoBitBP
from correlating_bp import CorrelatingBP
from gshare_bp import GShareBP
from profile_bp import ProfileBP

table_size = 2048
register_size = 9

# Always taken with all benchmarks
with open ('results/always_taken_bench.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['benchmark', 'missrate'])     
 
    for trace_file in os.listdir(os.getcwd() + "/traces/"):
        sim = Simulator(os.getcwd() + '/traces/' + trace_file)

        predictor = AlwaysBP(1)
        result = sim.simulate(predictor)

        writer.writerow([trace_file[:-4].replace("_", ""), result])
        
        
# Always not taken with all benchmarks 
with open ('results/always_ntaken_bench.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['benchmark', 'missrate'])     
 
    for trace_file in os.listdir(os.getcwd() + "/traces/"):
        sim = Simulator(os.getcwd() + '/traces/' + trace_file)

        predictor = AlwaysBP(0)
        result = sim.simulate(predictor)

        writer.writerow([trace_file[:-4].replace("_", ""), result])
        
# One bit with all benchmarks 
with open ('results/onebit_bench.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['benchmark', 'missrate'])     
 
    for trace_file in os.listdir(os.getcwd() + "/traces/"):
        sim = Simulator(os.getcwd() + '/traces/' + trace_file)

        predictor = OneBitBP(table_size)
        result = sim.simulate(predictor)

        writer.writerow([trace_file[:-4].replace("_", ""), result])
     
# TwoBit with all benchmarks 
with open ('results/twobit_bench.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['benchmark', 'missrate'])     
 
    for trace_file in os.listdir(os.getcwd() + "/traces/"):
        sim = Simulator(os.getcwd() + '/traces/' + trace_file)

        predictor = TwoBitBP(table_size)
        result = sim.simulate(predictor)

        writer.writerow([trace_file[:-4].replace("_", ""), result])

# Correlated with all benchmarks 
with open ('results/corellating_bench.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['benchmark', 'missrate'])     
 
    for trace_file in os.listdir(os.getcwd() + "/traces/"):
        sim = Simulator(os.getcwd() + '/traces/' + trace_file)

        predictor = CorrelatingBP(table_size, register_size)
        result = sim.simulate(predictor)

        writer.writerow([trace_file[:-4].replace("_", ""), result])

#GShare with all benchmarks 
with open ('results/gshare_bench.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['benchmark', 'missrate'])     
 
    for trace_file in os.listdir(os.getcwd() + "/traces/"):
        sim = Simulator(os.getcwd() + '/traces/' + trace_file)

        predictor = GShareBP(table_size, register_size)
        result = sim.simulate(predictor)

        writer.writerow([trace_file[:-4].replace("_", ""), result])
 

#Profile with all benchmarks 
with open ('results/profile_bench.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['benchmark', 'missrate'])     
 
    for trace_file in os.listdir(os.getcwd() + "/traces/"):
        sim = Simulator(os.getcwd() + '/traces/' + trace_file)

        predictor = ProfileBP(table_size, register_size, sim.traces, 60)
        result = sim.simulate(predictor)

        writer.writerow([trace_file[:-4].replace("_", ""), result])
 
