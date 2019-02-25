import time
import numpy as np

x=np.zeros((10000,10000))

for k in [100,500,1000,2000,4000,8000]:
 start_time = time.time()
 for j in range(100):
  for i in range(k):
    x[i][j] = 2 * x[i][j];

 print("Execution Time for i = %d is %lf" %(k,time.time() - start_time))

