from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2,2)
qc.h(0)
qc.cx(0,1)
qc.measure([0,1], [0,1])

sim = AerSimulator()
result = sim.run(qc).result()
count = result.get_counts()

print(qc.draw())
print(count)
