#!/usr/bin/python
# -*- coding: utf-8 -*-
# filename : 'absorbeur-dynamique-accordé\k-m-freq.py'

import numpy as np 
import pylab as plt

PI = np.pi

# --- Masse mobile ---
# Acier:
rho_a = 7840. # kg/m^3
E_a = 2.*(10.**11)

# Dimensions:
Lm = 1. # longueur (m)
hm = 1. # largeur (m)
bm = 1. # hauteur (m)

Vm = Lm * hm * bm

# Masse
m1 = Vm*rho_a


# --- Lames ---
# Dimensions:
L = 1. # longueur (m)
b = 1. # largeur (m)
h = 1. # hauteur (m)

# Raideur:
kL = E_a*b*(h/L)**3 # raideur d'UNE SEULE LAME
k1 = 4.*kL

# Fréquence propre du système:
f = (1./(2.*PI)) * np.sqrt(k1/m1)

print('\nm1 = {0}\n\nk1 = {1}\n\nf = {2}\n\n'.format(m1, k1, f))
