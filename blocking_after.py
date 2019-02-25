import time
import numpy as np

x = np.zeros((500,500))
y = np.zeros((500,500))
z = np.zeros((500,500))

l = [10,20,40,80,160,320]
b = [1,2,4,8,16,32,64]

for m in l:
 for n in b:
  start_time = time.time()
  for jj in range(0,m,n):
   for kk in range(0,m,n):
    for i in range(m):
     for j in range(jj,min(jj+n,m)):
      r = 0; 
      for k in range(kk,min(kk+n,m)):
       r = r + y[i][k]*z[k][j]; 
      x[i][j] = x[i][j] + r;
 
  print("Execution Time for N = %d and B = %d is %lf" %(m,n,time.time() - start_time))
