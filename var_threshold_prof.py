import os
import csv
from simulator import Simulator
from profile_bp import ProfileBP

table_size = 2048
register_size = 9

with open ('results/profile_varied_thres.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['benchmark', 'threshold', 'missrate'])     
    
    for trace_file in os.listdir(os.getcwd() + "/traces/"):
        for threshold in range(50, 100):
            sim = Simulator(os.getcwd() + '/traces/' + trace_file)

            predictor = ProfileBP(table_size, register_size, sim.traces, threshold)
            profile_result = sim.simulate(predictor)

            writer.writerow([trace_file[:-4].replace("_", ""), threshold, profile_result])
           


     
         
 
