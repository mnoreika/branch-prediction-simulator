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

register_size = 3

with open ('results/varied_sim.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    writer.writerow(['table_size', 'always_taken', 'always_ntaken',
            'one_bit', 'two_bit', 'correlated', 'gshare']) 

    for table_size in [512, 1024, 2048, 4096]:
        predictor = AlwaysBP(1)
        always_taken_result = sim.simulate(predictor)

        predictor = AlwaysBP(0)
        always_ntaken_result = sim.simulate(predictor)

        predictor = OneBitBP(table_size)
        one_bit_result = sim.simulate(predictor)

        predictor = TwoBitBP(table_size)
        two_bit_result = sim.simulate(predictor)
    
        predictor = CorrelatingBP(table_size, register_size)
        correlated_result = sim.simulate(predictor)

        predictor = GShareBP(table_size, register_size)
        gshare_result = sim.simulate(predictor)

        writer.writerow([table_size, always_taken_result, always_ntaken_result,
            one_bit_result, two_bit_result, correlated_result, gshare_result])
    
