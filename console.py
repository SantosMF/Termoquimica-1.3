#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 14:49:49 2021

@author: marcio
"""
import modulo
import readline
readline.parse_and_bind('tab: complete')
scfout = str(input('Insira o arquivo scf.out:\n>> '))
dynout = str(input('Insira o arquivo dyn.out:\n>> '))
temp =  str(input('Insira as temperaturas mínima, máxima e deltaT (valores separados por espaço):\n>> '))
sistema = str(input('Sólidos ou Moléculas/Átomos? (s ou m):\n>> '))
Tmin = temp.split()[0]
Tmax = temp.split()[1]
dT = temp.split()[2]
if sistema == 's':
    valores = ['solido', scfout, dynout, Tmin, Tmax, 0, 0, 0, dT]
    resultado = modulo.Termo(valores)
    print(resultado)
    with open(str(input('salvar dados como? (insira nome com extensão)\n>> ')),'w') as out:
        out.write(resultado)
elif sistema == 'm':
    tipo = str(input('Linear, não-linear ou monoatômico? (l, nl, ma):\n>> '))
    if tipo == 'l':
        S = int(input('Número de simetria? \n>> '))
        P = float(input('Pressão? (em atm):\n>> '))
        valores = ['molecula', scfout, dynout, Tmin, Tmax, P, S,'linear' , dT]
        resultado = modulo.Termo(valores)
        print(resultado)
        with open(str(input('salvar dados como? (insira nome com extensão)\n>> ')),'w') as out:
            out.write(resultado)
    if tipo == 'nl':
        S = int(input('Número de simetria? \n>> '))
        P = float(input('Pressão? (em atm):\n>> '))
        valores = ['molecula', scfout, dynout, Tmin, Tmax, P, S,'nolinear' , dT]
        resultado = modulo.Termo(valores)
        print(resultado)
        with open(str(input('salvar dados como? (insira nome com extensão)\n>> ')),'w') as out:
            out.write(resultado)
    elif tipo == 'ma':
        P = float(input('Pressão? (em atm):\n>> '))
        valores = ['molecula', scfout, dynout, Tmin, Tmax, P, S, 'atomo', dT]
        resultado = modulo.Termo(valores)
        print(resultado)
        with open(str(input('salvar dados como? (insira nome com extensão)\n>> ')),'w') as out:
            out.write(resultado)
