from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator 

qc = QuantumCircuit(3,3)
qc.h(0)
qc.cx(0,1)
qc.z(2)
qc.measure([0,1,2], [0,1,2])

sim = AerSimulator()
result = sim.run(qc, shots=1024).result()
counts = result.get_counts()

print(qc.draw())
print(counts)
