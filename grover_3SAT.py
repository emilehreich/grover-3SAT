'''
    @file: grover_3SAT.py

    @date: 15/05/2022

    @author: Emile Janho Dit Hreich (309994)
             emile.janhodithreich@epfl.ch

             Arion Zimmerman
             arion.zimmermann@epfl.ch (315007)

    @brief: Mini-Projet quantique 2022

'''
# =============================================================================================
# Libraries

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer, IBMQ
from qiskit.visualization import *
from qiskit.compiler import transpile, assemble
import numpy as np

# =============================================================================================
# Account loading
provider = IBMQ.load_account()

# =============================================================================================
# Problem instance

# Question 1
def naive_enumeration():
    solutions = []

    for bit_list in range(0, 7):
        x = bit_list & 0b1
        y = (bit_list >> 1) & 0b1
        z = (bit_list >> 2) & 0b1

        if ((~x | ~y | ~z) &
            (~x | ~y |  z) &
            (~x | y  |  z) &
            (x  | ~y |  z) &
            (x  | y  | ~z) &
            (x  | y  |  z)) == 1:
                solutions.append((x, y, z))

    print(solutions)


# Question 2
def oracle_uf(circuit):
    # N = 8
    # M = 2
    # Define \theta as \arcsin(\sqrt \frac{M}{N})
    # We must iterate K = [\frac{\pi}{4 \theta_0}] times

    # ex1() yields the solutions s_1 = (1, 0, 1) and s_2 (0, 1, 1)

    circuit.ccx(0, 2, 3)
    circuit.ccx(1, 2, 3)

# Question 3
def reflection():
    '''
        The reflection operator
    '''
    pass

# Question 5
def direct_Uf():
    pass
    # Add an ancilla qubit
    # Apply Hadamard to initial state with ancilla = 0
    # Apply Uf (as in ex2)
    # Project with |xyz><abc| transformation where abc is Hadamard basis


# =============================================================================================
# helper functions

def gen_hadamard(circuit, qubits):
    """Apply a H-gate to 'qubits' in qc"""
    for q in qubits:
        circuit.h(q)
    return circuit

# Generic functions
def simulate(circuit, shots):
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots)
    result = job.result()
    counts = result.get_counts(circuit)

    print(counts) # TODO

# =============================================================================================
# Main

if __name__ == "__Main__":

    # ----------------------------------------
    # Q1: naive enumeration
    naive_enumeration()

    # ----------------------------------------
    # circuit implementation

    qubits  = 3
    nb_bits = 4

    # initialize circuit
    circuit = QuantumCircuit(nb_bits, qubits)

    # initial state
    gen_hadamard(circuit, nb_bits)

    circuit.barrier(np.arange(0,4))

    # add oracle U_f
    oracle_uf(circuit)

    # add reflector operator
