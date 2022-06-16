#!/usr/bin/env python3
# -*- coding: utf-8 -*-
eletronic = 'Electronic Energy'
point = 'Zero point energy'
language = 'Language'
copy = 'Copy'
copy1 = 'Copy text to clipboard'
save1 = 'Save as .dat'
edit1 = 'Make text area editable'
calcule1 = 'Calculate thermodynamic functions'
warning = 'Info'
title = 'Thermochemistry-1.3'
file = 'File'
fecha  = 'Close'
ajuda = 'Help'
save = 'Save'
edit = 'Edit'
sobre = 'About'
exibir ='Display'
calcule = 'Calculate'
path_scf = 'Insert the ".out" file of the scf calculation'
path_dyn = 'Insert the ".out" file of the dynmat.x calculation'
tmin = 'Minimum'
tmax = 'Maximum'
controle = 'Thermodynamic Functions'
tD = 'Delta T'
tK = 'Temperature in Kelvin'
sol = 'Solids'
mol = 'Molecules/atoms'
Nsym = 'Symmetric number'
Pres = 'Pressure (atm)'
line = 'Linear'
poli = 'non-linear'
mono = 'Atoms/Ions'
erro = 'Error!'
erro1 = 'One or more files were not inserted'
completo = 'Complete'
tempU = 'Temperature x E_internal'
tempS = 'Temperature x Entropy'
tempH = 'Temperature x Enthalpy'
tempG = 'Temperature x E_Gibbs'
tempA = 'Temperature x E_Helmholtz'
abrir = 'Open file'
saveas = 'Save as'
ferramentas = 'Tools'
simetria = 'Symmetric number'
conv = 'Conversion factors'
msg = 'help'



f2 = 'Instructions for use, press F2.'
info = 'Software for calculating thermodynamic functions\n\
    author: Márcio F. Santos \nemail: marcio.santos@ice.ufjf.br'
texto =  """
# USAGE NOTES
Software programmed to read output files from Quantum Espresso versions 6x.
Minimum temperature must be different from the maximum temperature. If you want to plot the results for only one value of T, do as follows:

            Tmin; (Tmax = Tmin + Delta T); Delta T

After entering the data, just click on calculate and the data will be displayed in the text area.

Shortcut keys to display functions separately: (View Menu)

            F7 = 'Temperature x E_internal'
            F8 = 'Temperature x Entropy'
            F9 = 'Temperature x Enthalpy'
            F10 = 'Temperature x E_Gibbs'
            F11 = 'Temperature x E_Helmholtz'

To save the data shown on the screen, just click on the save button, provide a name for the file and set the directory for it.

By default, the text area is set to read-only. If you want to edit the data, just click on the "Edit" button.

more information read the README.md file"""

texto2 =''' # Symmetry number for some molecules
H2O  \t 2
CO2  \t 1
C6H6 \t 12
H2   \t 2
O2   \t 2
N2   \t 2
HCl  \t 1
HBr  \t 1
HI   \t 1
'''
texto3 ='''
1.0 Ry:
        = 0.5 hartree
        = 13.605691930242388 eV
        = 1312.7496997450642 kJ/mol
        = 313.75470835207074 kcal/mol
        = 2.17987197e-21 kJ
        = 5.21001904875717e-22 kcal'''
info1 = 'Text copied to clipboard'
info2 = 'There is no text to copy'
