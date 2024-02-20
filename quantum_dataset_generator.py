from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
import numpy as np

# Function to apply single qubit rotations for each qubit based on parameterized symbols
def apply_single_qubit_rotations(qc, qubit, params):
    """Apply parameterized rotations to a single qubit in a Qiskit circuit.

    Args:
        qc (QuantumCircuit): The Qiskit quantum circuit.
        qubit (int): Index of the qubit to apply rotations to.
        params (list): List of three Parameters for RX, RY, RZ rotations.
    """
    qc.rx(params[0], qubit)
    qc.ry(params[1], qubit)
    qc.rz(params[2], qubit)

# Function to create an entangling layer using CZ gates
def create_entangling_layer(qc, qubits):
    """Generate a layer of CZ gates to entangle qubits in a Qiskit circuit.

    Args:
        qc (QuantumCircuit): The Qiskit quantum circuit.
        qubits (list): List of qubit indices to entangle.
    """
    for i in range(len(qubits) - 1):
        qc.cz(qubits[i], qubits[i + 1])
    if len(qubits) > 2:
        # Add a CZ gate between the first and last qubit for circuits larger than 2 qubits
        qc.cz(qubits[0], qubits[-1])

# Function to generate the quantum circuit
def generate_quantum_circuit(n_qubits, n_layers):
    """Generate a quantum circuit with parameterized single qubit rotations and entangling layers using Qiskit.

    Args:
        n_qubits (int): Number of qubits for the circuit.
        n_layers (int): Number of layers in the circuit.

    Returns:
        QuantumCircuit: The generated Qiskit quantum circuit.
    """
    qc = QuantumCircuit(n_qubits)
    params = [[Parameter(f'theta_{layer}_{qubit}_{angle}') for angle in range(3)] for qubit in range(n_qubits) for layer in range(n_layers + 1)]

    for layer in range(n_layers):
        for qubit in range(n_qubits):
            apply_single_qubit_rotations(qc, qubit, params[layer * n_qubits + qubit])
        create_entangling_layer(qc, list(range(n_qubits)))

    # Apply final layer of rotations
    for qubit in range(n_qubits):
        apply_single_qubit_rotations(qc, qubit, params[n_layers * n_qubits + qubit])

    return qc

# Example usage
n_qubits = 4  # Define 4 qubits
n_layers = 3  # Specify the number of layers in the circuit
qc = generate_quantum_circuit(n_qubits, n_layers)

# Display the circuit
print("Generated Quantum Circuit:")
print(qc.draw())
