# Algo_1_Test.py
from qiskit import QuantumCircuit, transpile, Aer, assemble
from qiskit.visualization import plot_histogram

# Initialiser le simulateur quantique
simulator = Aer.get_backend('aer_simulator')

# Créer un circuit quantique de 2 qubits et 2 bits classiques
qc = QuantumCircuit(2, 2)

# Ajouter des portes quantiques (Hadamard et CNOT)
qc.h(0)
qc.cx(0, 1)

# Mesurer les qubits
qc.measure([0, 1], [0, 1])

# Transpiler et assembler le circuit
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)

# Exécuter le circuit sur le simulateur
result = simulator.run(qobj).result()

# Obtenir les résultats de la mesure
counts = result.get_counts(compiled_circuit)
print(counts)

# Optionnel : Visualiser les résultats
plot_histogram(counts)
