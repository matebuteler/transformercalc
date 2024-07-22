'''

1) Core area (Sn)
2) Calculate the number of turns (N1, N2)
3) Primary and secondary currents (I1 , I2)
4) Primary and secondary wire diameter (dc1, dc2)
5) Primary and secondary winding width (ab1, ab2)
6) Primary and secondary winding length and resistance (Lc1, Lc2, Rc1, Rc2)
7) Voltage drop and number of turns correction (VR1, VR2, N1' and N2')
8) Losses and performace calculation (Pcu, Pfe, Ptotal and n)
'''

import math
import numpy

def Sn(P2): # Core area [cm^2]
    return math.sqrt(P2) # You can multiply by any number between 0.7 and 1.2 depending on the quality of the sheet. Here we're using 1
def SnR(P2):
    return (math.sqrt(math.sqrt(P2))) **2 *0.95
def N1(V1, f, Bm, Sn): # Number of turns of the primary winding
    return V1 / (4.44 * f * Bm * (Sn * 0.95) * 10**-8)
def N2(V2, f, Bm, Sn): # Number of turns of the secondary winding
    return V2 / (4.44 * f * Bm * (Sn * 0.95) * 10**-8)

def I1(P2, V1, n = 0.9, cosfi = 0.8): # Primary current
    return P2 / (V1 * n * cosfi)

def I2(P2, V2): # Secondary current
    return P2 / V2

def dc1(I1, currdens = 4): # Primary wire diameter
    return 2*math.sqrt(I1/currdens/math.pi) # currdens is the current density of the wire

def dc2(I2, currdens = 4): # Secondary wire diameter
    return 2*math.sqrt(I2/currdens/math.pi)

def ab1(dc1, N1, Sn): # Primary winding width
    return (N1 / (math.sqrt(Sn) / dc1)) * dc1
def ab2(dc2, N2, Sn): # Secondary winding width
    return (N2 / (math.sqrt(Sn) / dc2)) * dc2