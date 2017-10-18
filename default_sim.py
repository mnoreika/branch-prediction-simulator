import sys
from simulator import Simulator
from trace import Trace
from counter import Counter
from register import Register
from counter_pool import CounterPool
from always_bp import AlwaysBP
from onebit_bp import OneBitBP
from twobit_bp import TwoBitBP
from correlating_bp import CorrelatingBP
from gshare_bp import GShareBP
from profile_bp import ProfileBP


# Default values
table_size = 512
register_size = 9

if (len(sys.argv) > 1):
    trace_file = sys.argv[1]

if (len(sys.argv) > 2): 
    table_size = int(sys.argv[2])

if (len(sys.argv) > 3):
    register_size = int(sys.argv[3])

# Simulate branch predictors
sim = Simulator(trace_file)

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

predictor = ProfileBP(table_size, register_size, sim.traces)
profile_result = sim.simulate(predictor)

print ("AlwaysTaken: ", always_taken_result) 
print ("AlwaysNotTaken: ", always_ntaken_result)
print ("OneBit: ", one_bit_result)
print ("TwoBit: ", two_bit_result)
print ("Correlated: ", correlated_result)
print ("GShared: ", gshare_result)
print ("Profile: ", profile_result)




