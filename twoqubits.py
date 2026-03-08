from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.x(1)
qc.measure([0,1], [0,1])

sim = AerSimulator()
result = sim.run(qc).result()
counts = result.get_counts()

print(qc.draw())
print(counts)
