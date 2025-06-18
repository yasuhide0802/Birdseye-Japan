from qiskit import QuantumCircuit, Aer, execute


def run_bell_pair():
    """Run a simple circuit that creates a Bell pair and measures it."""
    # 2 qubits with 2 classical bits for measurement
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])

    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1024)
    result = job.result()
    counts = result.get_counts(qc)
    return counts


if __name__ == "__main__":
    counts = run_bell_pair()
    print("Measurement results:", counts)
