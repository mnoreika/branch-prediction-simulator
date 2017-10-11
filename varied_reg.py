import sys
import csv
from simulator import Simulator
from counter import Counter
from register import Register
from counter_pool import CounterPool
from always_bp import AlwaysBP
from onebit_bp import OneBitBP
from twobit_bp import TwoBitBP
from correlating_bp import CorrelatingBP
from gshare_bp import GShareBP

# Simulate branch predictors with varied table and register values
sim = Simulator(sys.argv[1])

table_size = 1024

with open ('results/varied_reg.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    writer.writerow(['register_size', 'correlated', 'gshare']) 
    
    for register_size in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]: 
        predictor = CorrelatingBP(table_size, register_size)
        correlated_result = sim.simulate(predictor)

        predictor = GShareBP(table_size, register_size)
        gshare_result = sim.simulate(predictor)

        writer.writerow([register_size, correlated_result, gshare_result])
    
