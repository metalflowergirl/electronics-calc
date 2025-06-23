import math
pi = float(3.1415926536)

#inductive_reactance = 2*pi*F*L
def XC():
    return capacitive_reactance
def XL():
    return inductive_reactance
#def power_current():
#    return 
choice = input("XC, XL, Voltage, exit, ")
if choice == "XC":
    F = float(input("Frequency in Hertz? "))
    C = float(input("Capacitance in Farads? "))
    capacitive_reactance = 1/(2*pi*F*C)
    print(capacitive_reactance)
if choice == "XL":
    F = float(input("Frequency in Hertz? "))
    L = float(input("Inductance in Henries? "))
    inductive_reactance = 2*pi*F*L
    print(inductive_reactance)
if choice == "Voltage":
    choice = input("Select method: I&R, P&I, P&R")
    if choice == "I&R":
        I = float(input("Cureent in Amperes? "))
        R = float(input("Resistance in Ohms? "))
        V = I*R
        print(V)
if choice == "exit":
    exit()
#else:
#   input()
#    if 
