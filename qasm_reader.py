from qiskit import QuantumCircuit

# Load a quantum circuit from a QASM file
with open("shors_circuit_demo.qasm", "r") as f:
    qasm_str = f.read()

# Recreate the quantum circuit from QASM
qc_from_qasm = QuantumCircuit.from_qasm_str(qasm_str)
