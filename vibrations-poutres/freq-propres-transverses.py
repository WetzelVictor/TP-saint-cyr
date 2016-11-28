#!/usr/bin/python
# -*- coding: utf-8 -*-
# filename : 'vibrations-poutres\freq-propres.py'

# Calcul fréquences propres poutre (AS-AS) et (E-L)

import numpy as np 
import pylab as plt


n = np.linspace(0,10,11)
PI = np.pi


""" === Ondes transverses: poutre E-L === """
# --- Caractéristiques pyhsiques
L1 = 1.   # Longueur (m)
rho1 = 1. # Masse volumique (kg/m^3)
E1 = 1.  # Module de Young (Pa)
I1 = 1.   # Moment de flexion
S1 = 1.   # Section de la poutre (m^2)

c_T = (E1*I1)/(S1*rho1)

# --- Calcule des fréquences propres exactes 'f':
fp_1_vraie = (1/(2*PI)) * (1.88/L1)**2 *np.sqrt(c_T)
fp_2_vraie = (1/(2*PI)) * (4.69/L1)**2 *np.sqrt(c_T)

# --- Calcule des fréquences propres approchées 'f':
fp_1_app = (1/(2*PI)) * (3.567/(L1**2)) * np.sqrt(c_T)
fp_2_app = (1/(2*PI)) * np.sqrt(c_T)

# --- Print: valeures arrondies
print 'Poutre E-L (transverse):\nFréquences propres:\n \n=THÉORIQUES= (Hz):\n\t1:  {0} \n\t2:  {1}'.format(fp_1_vraie, fp_2_vraie)

print '\n=RAYLEIGH-RITZ= (Hz):\n\t1: {0} \n\t'.format(fp_1_app)

