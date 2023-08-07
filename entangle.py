from qiskit import QuantumCircuit
from qiskit import execute
from qiskit import Aer


qc = QuantumCircuit(2)

qc.h(1)

qc.draw()

qc.cx(1,0)

svsim = Aer.get_backend('statevector_simulator')

result = execute(qc, svsim).result().get_statevector().draw()