# single_neuron.py
# Simple neuron simulation: membrane potential response

import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
time = np.linspace(0, 100, 1000)  # 100 ms, 1000 steps
V = np.zeros_like(time)            # Membrane potential array
V_rest = -65                       # Resting potential in mV
I = 10                             # Input current in arbitrary units

# Simple neuron dynamics (leaky integrate-and-fire)
tau = 10                            # Time constant
for i in range(1, len(time)):
    V[i] = V[i-1] + (-(V[i-1]-V_rest) + I) * (time[1]-time[0])/tau
    if V[i] >= 0:                  # Spike threshold
        V[i] = 50                  # Spike
        V[i-1] = V_rest            # Reset previous step

# Plot the membrane potential
plt.plot(time, V)
plt.title("Simple Neuron Simulation")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane Potential (mV)")
plt.show()
