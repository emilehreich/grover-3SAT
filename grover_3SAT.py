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
from qiskit.tools.jupyter import *
from qiskit.compiler import transpile, assemble
from ibm_quantum_widgets import *
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
def oracle_uf():
    # N = 8
    # M = 2
    # Define \theta as \arcsin(\sqrt \frac{M}{N})
    # We must iterate K = [\frac{\pi}{4 \theta_0}] times

    # ex1() yields the solutions s_1 = (1, 0, 1) and s_2 (0, 1, 1)

    Uf = np.array([[1, 0, 0, 1 ],
                   [0, 1, 0, 1 ],
                   [0, 0, 1, 0 ],
                   [1, 1, 0, 1 ]]) # The last vector was found as s_1 xor s_2

    return Uf

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


# Generic functions
def simulate(circuit, shots):
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots)
    result = job.result()
    counts = results.get_counts(circuit)

    print(counts) # TODO

# =============================================================================================
# Main

if __name__ == "__Main__":
    naive_enumeration()
