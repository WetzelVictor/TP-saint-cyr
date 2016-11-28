#!/usr/bin/python
# -*- coding: utf-8 -*-
# filename : 'vibrations-poutres\freq-propres.py'

import numpy as np 
import pylab as plt

PI = np.pi

""" --- Ondes longitudinales : libre- libre ---"""
# Calcul de la célérité c_L dans la poutre:
#    - Mesure la longueur
#	 - On détermine la première pulsations de résonnance (impact)
#    - Applique la formule

# --- Caractéristiques physiques de la poutre:
L = 1. # longueur (m)
f = 1. # 1ère Fréquence Propre (Hz)
w_1 = 2*PI*f
# --- Célérité des ondes longitudinales
c_L = L*w_1/PI

print 'Poutre L-L (longitudinales):\nCélérité c_L:  {0} (m/s)\n\n'.format(c_L)


