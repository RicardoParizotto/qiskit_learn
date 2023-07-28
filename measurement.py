from qiskit import QuantumCircuit
from qiskit.providers.aer import AerSimulator

qc = QuantumCircuit(3,3)    #quantum circuit o 3 qbits

qc.x([0,1]) #x gates on qbit 0 and 1

qc.measure([0,1,2], [0,1,2])



sim = AerSimulator()  #instantiate simulator

job = sim.run(qc)   #run the quantum circuit
result = job.result()   

result.get_counts()
qc.draw()