import os
import pyphi
import numpy as np

pyphi.config.load_file('../config/pyphi_config.yml')

tpm = np.array([
[0,0,0,0,0],[0,1,1,1,0],[0,0,1,1,1],[0,1,1,1,1],[1,0,0,1,1],[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1],[1,1,0,0,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,0,0],[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]
])


cm = np.array([
[0,1,1,1,0],
[0,0,1,1,1],
[1,0,0,1,1],
[1,1,0,0,1],
[1,1,1,0,0]
])

#distance_emd = pyphi.distance.emd(tpm,cm)
#distance_kmd = pyphi.distance.emd(tpm,cm)

labels = ('A', 'B', 'C' ,'D', 'E')
network = pyphi.Network(tpm, cm=cm, node_labels=labels)
state = (1,1,1,1,1)
node_indices = (0, 1, 2, 3, 4)
subsystem = pyphi.Subsystem(network, state, node_indices)
sia = pyphi.compute.sia(subsystem)
print("MIP: \n", sia.cut)
print("Phi: \n Φ = ", sia.phi)
print("Time: \n", sia.time,"s")