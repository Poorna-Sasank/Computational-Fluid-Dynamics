import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

#Material Properties
L = 0.5
k = 400
p = 10000
C = 200
# BC and IC values
Ti = 400 #IC
To = 25 #BC
Tl = 25 #BC


# Grid description
n = 51         #No. of nodes in space
t = 200         #Total Simulation time

#Creating a dataframe to store data efficiently
header=[]
for i in range(1,n+1):
    header.append("Node: %i" %i)
df = pd.DataFrame(columns=header)

# Necessary calculations
dx = L/(n - 1)
a = k/(p*C) 
dt = 0.2
r = (a * dt)/(pow(dx, 2))
x = np.linspace(0, L, n)
st = np.linspace(0, t, int(t/dt))

T = np.zeros(n) # Future Timestep
T_o = np.zeros(n) # Present Timestep

T_o[1:n-1] = Ti             #IC 
T_o[0] = 25; T_o[n-1] = 25   #BC


for k in range(0, int(t/dt)):
    df.loc[len(df.index)] = T_o
    for i in range(1, n - 1):
        T[i] = T_o[i] + r*(T_o[i - 1] - 2*T_o[i] + T_o[i + 1])
    T[0] = 25; T[n-1] = 25
    T_o, T = T, T_o
    #plt.plot(x, T)
    #plt.pause(pow(0.1, 50))
    
  
print(T)
print(df)

#Plots
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(x, df.loc[49, :], 'b', label = 't = 10s')
ax1.plot(x, df.loc[249, :], 'r', label = 't = 50s')
ax1.plot(x, df.loc[599, :], 'y', label = 't = 120s')
ax1.plot(x, T, 'g', label = 't = 200s')
ax1.set_xlabel('length, m')
ax1.set_ylabel('Temperature, deg C')
ax1.legend()

#for i, j in zip(x, T):
    #ax1.text(i, j, '({}, {})'.format(i, i))
# ax1.plot(x, df.loc[599, :])

ax2.plot(st, df.loc[:, 'Node: 10'])
ax2.set_xlabel('Time, s')
ax2.set_ylabel('Temperature, deg C')
df.to_excel('1DTransient_flow_computed_values.xlsx', index=False)
plt.show()

 
