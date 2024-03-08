from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import GroverOperator
from qiskit_aer import AerSimulator  # Updated import statement

# Define a proper oracle circuit
def create_oracle(n_qubits):
    qc = QuantumCircuit(n_qubits)
    # Example oracle: Marks the |11> state
    qc.cz(0, 1)  # Apply CZ gate to flip the phase of the |11> state
    return qc

n_qubits = 4

# Initialize the quantum circuit
qc = QuantumCircuit(n_qubits, n_qubits)

# Apply Hadamard gates to initialize the superposition state
qc.h(range(n_qubits))

# Create the oracle and diffusion operators for Grover's algorithm
oracle = create_oracle(n_qubits)
grover_op = GroverOperator(oracle)  # Directly use the oracle circuit

# Append Grover operator to the quantum circuit
qc.append(grover_op, range(n_qubits))

# Measurement
qc.measure(range(n_qubits), range(n_qubits))

# Display the circuit
print("Quantum Circuit with Grover's Algorithm:")
print(qc.draw())

# Export the circuit to a QASM file
qasm_str = qc.qasm()
qasm_file = "grovers_circuit_demo.qasm"
with open(qasm_file, "w") as f:
    f.write(qasm_str)
print(f"Quantum circuit exported to {qasm_file}")

# Simulate the circuit
simulator = AerSimulator()  # Use the updated import
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1024)
result = job.result()

# Plot the results
counts = result.get_counts()
plot_histogram(counts)
