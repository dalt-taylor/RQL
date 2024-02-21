from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import QFT
from qiskit_aer import AerSimulator

def c_amod15(a, power):
    """Controlled multiplication by a mod 15"""
    if a not in [2,7,8,11,13]:
        raise ValueError("'a' must be 2,7,8,11, or 13")
    U = QuantumCircuit(4)        
    for iteration in range(power):
        if a in [2,13]:
            U.swap(0,1)
            U.swap(1,2)
            U.swap(2,3)
        if a in [7,8]:
            U.swap(2,3)
            U.swap(1,2)
            U.swap(0,1)
        U.x(0)
    U = U.to_gate()
    U.name = f"{a}^{2**iteration} mod 15"
    c_U = U.control()
    return c_U

# Parameters
a = 7  # Base for the exponentiation
N = 15  # The number to factor

# Quantum Circuit Setup
n_qubits = 4  # Number of qubits in the exponent register, chosen for simplicity
qc = QuantumCircuit(n_qubits*2, n_qubits)  # Double the qubits for calculation, measurements for the exponent register

# Apply Hadamard gates to the exponent register for superposition
qc.h(range(n_qubits))

# Apply modular exponentiation
for q in range(n_qubits):
    qc.append(c_amod15(a, 2**q), [q] + [i + n_qubits for i in range(4)])

# Apply inverse QFT on the exponent register
qc.append(QFT(n_qubits, do_swaps=False).inverse(), range(n_qubits))

# Measurement
qc.measure(range(n_qubits), range(n_qubits))

# Display the circuit
print("Quantum Circuit with Modular Exponentiation:")
print(qc.draw())

# Export the circuit to a QASM file
qasm_str = qc.qasm()
qasm_file = "shors_circuit_demo.qasm"
with open(qasm_file, "w") as f:
    f.write(qasm_str)
print(f"Quantum circuit exported to {qasm_file}")

# Simulate the Circuit
simulator = AerSimulator()  # Use the AerSimulator
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1024)
result = job.result()

# Get the results and display the histogram
counts = result.get_counts(compiled_circuit)
plot_histogram(counts)
