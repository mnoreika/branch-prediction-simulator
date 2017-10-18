import os
import csv
from simulator import Simulator
from twobit_bp import TwoBitBP

with open ('results/twobit_varied_table.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['benchmark', 'tablesize', 'missrate'])     
    
    for trace_file in os.listdir(os.getcwd() + "/traces/"):
        for table_size in [512, 1024, 2048, 4096]:
            print (table_size)
 
            sim = Simulator(os.getcwd() + '/traces/' + trace_file)

            predictor = TwoBitBP(table_size)
            two_bit_result = sim.simulate(predictor)

            writer.writerow([trace_file[:-4].replace("_", ""), table_size, two_bit_result])
           


     
         
 
