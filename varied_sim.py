import sys
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

for table_size in [512, 1024, 2048, 4096]:
    print ("Table size: ", table_size)

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

    print ("AlwaysTaken: ", always_taken_result) 
    print ("AlwaysNotTaken: ", always_ntaken_result)
    print ("OneBit: ", one_bit_result)
    print ("TwoBit: ", two_bit_result)
    print ("Correlated: ", correlated_result)
    print ("GShared: ", gshare_result)




