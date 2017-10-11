from dynamic_programming import DP
from monte_carlo import MC
from emulator import Emulator
import matplotlib.pyplot as plt
import api


"""
Dynamic Programming
"""
# Initialization
DP = DP()
v_s0 = DP.run()
print("The performance of Dynamic Programming is : ", v_s0)

"""
Monte Carlo
"""
MC = MC()
q = []

for t in range(10, 100):
    v = MC.run(10000, t)
    print(v)
    q.append(v)

plt.plot(q)
plt.legend("Monte Carlo")
plt.show()
