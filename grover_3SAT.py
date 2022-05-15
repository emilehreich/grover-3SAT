'''
    @file: grover_3SAT.py

    @date: 15/05/2022

    @author: Emile Janho Dit Hreich (309994)
             emile.janhodithreich@epfl.ch

             Arion Zimmerman
             example@epfl.ch (XXXXXX)

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


# =============================================================================================
# Problem instance

# Question 2
def oracle_uf():
    '''
        The oracle gate Uf such that Uf |xyzc⟩ = |xyz⟩ ⊗ |c ⊕ f(xyz)⟩
    '''
    pass

# Question 3
def reflection():
    '''
        The reflection operator
    '''
    pass

# =============================================================================================
# Main

if __name__ == "__Main__":
    pass