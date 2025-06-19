import math
#input("What function?")
#if input == XC:
F = float(input("Frequency in Hertz"))
C = float(input("Capacitance in Farads"))
pi = float(3.1415926536)
capacitive_reactance = float(1/(2*pi*F*C))
print(capacitive_reactance,"Ohms")
#else: input("Function not found")
#if input == LC:
      #F = float(input("Frequency in Hertz"))
      #L = float(input("Inductance in Henrys"))
      #pi = float(3.1415926536)
      #inductive_reactance = float(2*pi*F*L)
      #print(inductive_reactance, "Ohms")
#else: input()
