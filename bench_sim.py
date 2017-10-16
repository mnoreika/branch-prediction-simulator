import os
import csv
from simulator import Simulator
from always_bp import AlwaysBP
from onebit_bp import OneBitBP
from twobit_bp import TwoBitBP
from correlating_bp import CorrelatingBP
from gshare_bp import GShareBP


table_size = 1024
register_size = 3

# Always taken with all benchmarks
with open ('results/always_taken_bench.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['benchmark', 'missrate'])     
 
    for trace_file in os.listdir(os.getcwd() + "/traces/"):
        sim = Simulator(os.getcwd() + '/traces/' + trace_file)

        predictor = AlwaysBP(1)
        always_taken_result = sim.simulate(predictor)

        writer.writerow([trace_file[:-4].replace("_", ""), always_taken_result])
        
        
# Always not taken with all benchmarks 
with open ('results/always_ntaken_bench.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['benchmark', 'missrate'])     
 
    for trace_file in os.listdir(os.getcwd() + "/traces/"):
        sim = Simulator(os.getcwd() + '/traces/' + trace_file)

        predictor = AlwaysBP(0)
        always_taken_result = sim.simulate(predictor)

        writer.writerow([trace_file[:-4].replace("_", ""), always_taken_result])
        
# One bit with all benchmarks 
with open ('results/onebit_bench.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['benchmark', 'missrate'])     
 
    for trace_file in os.listdir(os.getcwd() + "/traces/"):
        sim = Simulator(os.getcwd() + '/traces/' + trace_file)

        predictor = OneBitBP(table_size)
        always_taken_result = sim.simulate(predictor)

        writer.writerow([trace_file[:-4].replace("_", ""), always_taken_result])
     
# TwoBit with all benchmarks 
with open ('results/twobit_bench.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['benchmark', 'missrate'])     
 
    for trace_file in os.listdir(os.getcwd() + "/traces/"):
        sim = Simulator(os.getcwd() + '/traces/' + trace_file)

        predictor = TwoBitBP(table_size)
        always_taken_result = sim.simulate(predictor)

        writer.writerow([trace_file[:-4].replace("_", ""), always_taken_result])

# Correlated with all benchmarks 
with open ('results/corellating_bench.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['benchmark', 'missrate'])     
 
    for trace_file in os.listdir(os.getcwd() + "/traces/"):
        sim = Simulator(os.getcwd() + '/traces/' + trace_file)

        predictor = CorrelatingBP(table_size, register_size)
        always_taken_result = sim.simulate(predictor)

        writer.writerow([trace_file[:-4].replace("_", ""), always_taken_result])

#GShare with all benchmarks 
with open ('results/gshare_bench.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['benchmark', 'missrate'])     
 
    for trace_file in os.listdir(os.getcwd() + "/traces/"):
        sim = Simulator(os.getcwd() + '/traces/' + trace_file)

        predictor = GShareBP(table_size, register_size)
        always_taken_result = sim.simulate(predictor)

        writer.writerow([trace_file[:-4].replace("_", ""), always_taken_result])
 


