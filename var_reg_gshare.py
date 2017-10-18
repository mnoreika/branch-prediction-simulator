import os
import csv
from simulator import Simulator
from gshare_bp import GShareBP

table_size = 8192

with open ('results/gshare_varied_reg.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['benchmark', 'registersize', 'missrate'])     
    
    for trace_file in os.listdir(os.getcwd() + "/traces/"):
        for register_size in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            sim = Simulator(os.getcwd() + '/traces/' + trace_file)

            predictor = GShareBP(table_size, register_size)
            two_bit_result = sim.simulate(predictor)

            writer.writerow([trace_file[:-4].replace("_", ""), register_size, two_bit_result])
           


         
 
