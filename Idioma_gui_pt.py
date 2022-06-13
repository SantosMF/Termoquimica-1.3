#!/usr/bin/env python3
# -*- coding: utf-8 -*-
eletronic = 'Energia Eletrônica'
point = 'Energia de ponto zero'
language = 'Idioma'
copy = 'Copiar'
copy1 = 'Copia texto para área de transferência'
save1 = 'Salvar como arquivo .dat'
edit1 = 'Tornar área de texto editável'
calcule1 = 'Calcular funções termodinâmicas'
warning = 'Info'
title = 'Termoquimica-1.3'
file = 'Arquivo'
fecha  = 'Fechar'
ajuda = 'Ajuda'
save = 'Salvar'
edit = 'Editar'
sobre = 'Sobre'
exibir ='Exibir'
calcule = 'Calcular'
path_scf = 'Insira o arquivo .out do cálculo scf'
path_dyn = 'Insira o arquivo .out do cálculo dynmat.x'
tmin = 'Mínima'
tmax = 'Máxima'
controle = 'Funções Termodinâmicas'
tD = 'Delta T'
tK = 'Temperatura em Kelvin'
sol = 'Sólidos'
mol = 'Moléculas/átomos'
Nsym = 'Número de simetria'
Pres = 'Pressão (atm)'
line = 'Linear'
poli = 'não-linear'
mono = 'Átomos/íons'
erro = 'Erro!'
erro1 = 'Um ou mais arquivos não foram inseridos'
completo = 'Completo'
tempU = 'Temperatura x E_interna'
tempS = 'Temperatura x Entropia'
tempH = 'Temperatura x Entalpia'
tempG = 'Temperatura x E_Gibbs'
tempA = 'Temperatura x E_Helmholtz'
abrir = 'Abrir arquivo'
saveas = 'Salvar como'
ferramentas= 'Ferramentas'
simetria = 'Nº Simetria'
conv = 'Fatores de conversão'
msg = 'ajuda'
f2 = 'Instruções de uso, aperte F2.'
info = 'Software para cálcular funções termodinâmicas\n\
    autor: Márcio F. Santos \nemail mpraquedista@gmail.com'
texto = """
# NOTAS DE USO
Software programado para ler arquivos de saída das versões 6x do Quantum Espresso.
Temperatura mínima obrigatóriamente deve ser diferente da temperatura máxima. Caso deseje plotar os resultados para apenas um valor de T, faça da seguinte forma:

            Tmin; (Tmax = Tmin + Delta T); Delta T

Após inserir os dados, basta clicar em calcular que os dados serão exibidos na área de texto.

teclas de atalho para exibir funções separadamente: (Menu Exibir)

            F7  = 'Temperatura x E_interna'
            F8  = 'Temperatura x Entropia'
            F9  = 'Temperatura x Entalpia'
            F10 = 'Temperatura x E_Gibbs'
            F11 = 'Temperatura x E_Helmholtz'

Para salvar os dados que estão mostrados na tela basta clicar no botão salvar, fornecer um nome para o arquivo e setar o diretório para ele.

Por padrão, a área de texto é definida como somente leitura. Caso deseje editar os dados basta clicar no botão "Editar".

mais informações leia o arquivo README.md"""
texto2 =''' # Número de simetria para agumas moléculas
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
info1 = 'Texto copiado para área de transferência'
info2 = 'Não há texto para copiar'
