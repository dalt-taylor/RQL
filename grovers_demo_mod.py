from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import GroverOperator
from qiskit_aer import AerSimulator

# Define the oracle circuit directly
def create_oracle(n_qubits):
    # Define a circuit with 4 qubits and no ancillas
    oracle_circuit = QuantumCircuit(n_qubits)
    # Apply CZ gate to flip the phase of the |0011> state
    oracle_circuit.cz(0, 2)
    oracle_circuit.cz(1, 2)
    # Convert the circuit to a gate with a label
    return oracle_circuit

n_qubits = 4

# Initialize the quantum circuit
qc = QuantumCircuit(n_qubits, 2)  # Only measure 2 qubits for partial search

# Apply Hadamard gates to initialize the superposition state
qc.h(range(n_qubits))

# Create the oracle for Grover's algorithm
oracle_circuit = create_oracle(n_qubits)
# Use the oracle circuit directly with GroverOperator
grover_op = GroverOperator(oracle=oracle_circuit)

# Append Grover operator to the quantum circuit
qc.append(grover_op, range(n_qubits))

# Measurement: Only measure the 2 most significant qubits to determine the block
qc.measure([2, 3], [0, 1])

# Display the circuit
print("Quantum Circuit with Partial Grover's Algorithm:")
print(qc.draw())

# Export the circuit to a QASM file
qasm_str = qc.qasm()
qasm_file = "grovers_partial_mod.qasm"
with open(qasm_file, "w") as f:
    f.write(qasm_str)
print(f"Quantum circuit exported to {qasm_file}")

# Simulate the circuit
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1024)
result = job.result()

# Plot the results
counts = result.get_counts()
plot_histogram(counts)
