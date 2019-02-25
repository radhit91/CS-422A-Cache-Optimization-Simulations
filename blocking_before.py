import time
import numpy as np

x = np.zeros((500,500))
y = np.zeros((500,500))
z = np.zeros((500,500))

l = [10,20,40,80,160,320]

for m in l:
 start_time = time.time()
 for i in range(m):
  for j in range(m):
    r = 0;
    for k in range(m):
     r = r + y[i][k]*z[k][j];
     x[i][j] = r;
 
 print("Execution Time for N = %d is %lf" %(m,time.time() - start_time))
