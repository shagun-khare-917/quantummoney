from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import IBMQ, Aer, transpile, assemble
from qiskit.visualization import plot_histogram, plot_bloch_multivector, array_to_latex
from qiskit.extensions import Initialize
from numpy.random import randint
import numpy as np
print("Imports Successful")


def create_money(bits, bases):
    message = []
    for i in range(3):
        qc = QuantumCircuit(1,1)
        if bases[i] == 0: # Prepare qubit in Z-basis
            if bits[i] == 0:
                pass 
            else:
                qc.x(0)
        else: # Prepare qubit in X-basis
            if bits[i] == 0:
                qc.h(0)
            else:
                qc.x(0)
                qc.h(0)
        qc.barrier()
        message.append(qc)
    return message
    
bank_fixednote = np.array([1,0,0])
bank_fixedbase = np.array([0,1,1])

banknote = create_money(bank_fixednote, bank_fixedbase)

bank_bases = randint(2, size=3)


def measure_message(message, bases):
    backend = Aer.get_backend('aer_simulator')
    measurements = []
    for q in range(3):
        if bases[q] == 0: # measuring in Z-basis
            message[q].measure(0,0)
        if bases[q] == 1: # measuring in X-basis
            message[q].h(0)
            message[q].measure(0,0)
        aer_sim = Aer.get_backend('aer_simulator')
        qobj = assemble(message[q], shots=1, memory=True)
        result = aer_sim.run(qobj).result()
        measured_bit = int(result.get_memory()[0])
        measurements.append(measured_bit)
    return measurements
    
    
prob = 42
shots = 100

for i in range(100):
    forge_bits = randint(2, size=3)
    forge_bases = randint(2, size=3)
    forge_note = create_money(forge_bits, forge_bases)
    bank_measure = measure_message(forge_note, bank_bases)    
    bank_fixed = measure_message(banknote, bank_fixedbase)
    if(bank_fixed==bank_measure):
        print("Bank Serial Number: " + str(bank_fixed))
        print("Verfied Bill: " + str(bank_measure))
    else:
        print("Bank Serial Number: " + str(bank_fixed))
        print("Forged Bill: " + str(bank_measure))
        prob = prob+1
    print("")

print("Probability of bills being forged:" + str(42/shots))


