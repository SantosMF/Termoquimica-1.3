#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#     Módulo para computar as contribuições termodinâmicas
from numpy import e, pi, log, sqrt, array, arange
import os
import Idioma_gui_en as lang
path = os.path.dirname(os.path.realpath(__file__))
#-------Constantes usadas-----------------------------------------------------
k = 1.380649e-23 # constante de Boltzmann J/K
h = 6.62607015e-34 # constante de Plank J.s ou J.Hz^-1
hbar = 1.054571817e-34 #constante de Planck reduzida  J.s
c = 299792458 # velocidade da luz no vácuo  m/s
R = 8.314462618 # constante molar dos gases J.mol^-1.K^-1
N_A = 6.02214076e+23 # constante de Avogadro mol^-1
MM = 1.660530000e-27 ##fator de conversão massa molecular em Kg
rbohr = 1.8897261246257702 ## raio de Bohr em angstrom
#----------------FUNÇÃO PARA LER O ARQUIVO DYNMAT.OUT-------------------------
def DynRead(dynmat):
    cm = [] ## lista contendo as frequencias em Hz
    with open(dynmat, 'r') as mat_out:
        for lines in mat_out:
            if 'mode' in lines:
                break
        try:
            for lines in mat_out:
                dados = lines.split()
                cm.append(float(dados[1])) # modos vibracionais em cm^-1
        except:
            pass
    if cm != []:
        frequencias = 100*array(cm) # cm^-1 to m^-1
    else:
        frequencias = None
    return frequencias # modos vibracionais em m^-1
#-------------FUNÇÃO PARA LER O ARQUIVO SCF.OUT-------------------------------
def ScfRead(scf_out):
    atomos = [] # símbolo dos átomos
    x = [] # coordenadas x
    y = [] # coordenadas y
    z = [] # coordenadas z
    label = [] # lista com todos os atomos da estrutura
    atom = {} # dicionário contendo átomos e massas
    nat = 0 ## número de átomos na célula ## variável global
    ntp = 0 ## número de tipos de átomos ## variável global
    celldm = 0
#-----------------abre o arquivo no modo leitura------------------------------
    with open(scf_out, 'r') as outscf:
        for lines in outscf:
            if 'number of atoms/cell' in lines:
                nat += int(lines[40:45]) ## modifica o valor da variável nat
                ntp += int((outscf.readline().rstrip().split('='))[1]) #
            if 'celldm(1)' in lines:
                celldm = float(lines[17:28])
            if 'mass' in lines: ## busca os tipos de átomos
                for i in range(0, ntp):
                    key = outscf.readline().split()
                    atomos.append(key[0])
                    atom[key[0]] = MM*float(key[2]) #  u.m.a to kg
            if 'Cartesian axes' in lines:
                outscf.readline(), outscf.readline()
                break
        try:
            for lines in outscf:
                dados = lines.split()
                label.append(dados[1]) # armazena os símbolos dos átomos
                x.append(float(dados[6])*celldm/rbohr) # armazena coordenadas x
                y.append(float(dados[7])*celldm/rbohr) # armazena coordenadas y
                z.append(float(dados[8])*celldm/rbohr) # armazena coordenadas z
               # if 'number of k points' in lines:
                #    break
        except:
            pass
        for lines in outscf:
            if "!" in lines: # localiza a energia eletrônica1312.7497558593593
                E_elec = (float(lines[32:50])*1312.7496997450642) # kcal/mol
#---------------término da leitura arquivo *.scf.out--------------------------
    massa = 0
    for i in label:
        massa = massa + atom[i]
    return  E_elec, massa, atom, label, x, y, z
##############################################################################
#-------------------------contribuições vibracionais--------------------------
def Evib(T, m): # m = modos vibracionais em m^-1
    if T == 0:
        e_vib = 0
    else:
        e_vib = 0
        for w in m: # energias vibracionais
            if w != 0.0:
                e_vib = e_vib + ((h*c*w)/((e**((h*c*w)/(k*T)))-1)) ##ok
        e_vib = e_vib/1000*N_A ## kJ/K*mol
    return e_vib
def Svib(T, m): # m = modos vibracionais em m^-1
    if T == 0:
        svib = 0
    else:
        svib = 0
        for w in m:
            if w != 0:
                teta = h*c*w/k ## teperatura vibracional K
                svib = svib + ((teta/T)/(e**(teta/T)-1)-log(1-e**(-teta/T)))
        svib = svib*R/1000 ## kJ/K*mol
    return svib
#---------------------------contribuições translacionais----------------------
def Etrans(T):
    e_trans = (3/2)*k*T
    return e_trans/1000*N_A ## kJ/mol
def Strans(T, P, M):
    if T == 0:
        s_trans = 0
    else:
        s_trans = k*(log(((2*pi*M*k*T)/h**2)**1.5 * (k*T)/P)+2.5)
        s_trans = s_trans/1000*N_A ## kJ/mol
    return s_trans
#---------------------------contribuições rotacionais-------------------------
def Erot(T, tipo):
    if tipo == 'linear':
        e_rot = k*T
    elif tipo == 'nolinear':
        e_rot = (3/2)*k*T
    elif tipo == 'atomo':
        e_rot = 0
    return e_rot/1000*N_A  ## kJ/mol
def Srot(T, Trot, TrotX, TrotY, TrotZ, sigma, tipo): # M = massa em kg
    if T == 0:
        s_rot = 0
    else:
        if tipo == 'linear':
            s_rot = (k + k*log((1.0/sigma)*(T/Trot)))/1000*N_A # J/K to kJ/mol*K
        elif tipo == 'nolinear':
            s_rot = ((3/2)*k + k*log((sqrt(pi)/sigma)*((T**(3/2))/sqrt(TrotX*TrotY*TrotZ))))/1000*N_A # J/K to kJ/mol*K
        elif tipo == 'atomo':
            s_rot = 0
    return s_rot ## kJ/K*mol
#=====================Função que recebe os dados da gui======================#
#               valores[0] == solido ou molécula                             #
#               valores[1] == path do arquivo scf.out                        #
#               valores[2] == path  do arquivo out dynmat.x                  #
#               valores[3] == temperatura mínima                             #
#               valores[4] == temperatura máxima                             #
#               valores[5] == pressão                                        #
#               valores[6] == número de simetria                             #
#               valores[7] == não-linear, linear ou átomo                    #
#               valores[8] == Delta T                                        #
#============================================================================#
def Termo(valores): ## valores --> tupla com os dados recebidos da gui
    scf = ScfRead(valores[1]) # dados extraidos do arquivo scf.out
    m = DynRead(valores[2]) # array com os modos vibracionais em m^-1
    Eel = float(scf[0]) # energia eletrônica em kJ/mol
    E_zpe = sum(0.5*h*c*m)/1000*N_A # retorna a energia de ponto zero
    M = float(scf[1]) # massa em kg
    atom, label, x, y, z = scf[2], scf[3], scf[4], scf[5], scf[6]
    sist  = str(valores[0]) # sólido ou molécula
    Tmin  = float(valores[3]) # temperatura mínima
    Tmax  = float(valores[4]) # temperatura máxima
    dT    = float(valores[8]) # diferença de temperatura
    P     = float(valores[5])*101325 ## atm para pascal
    sigma = int(valores[6]) # número de simetria
    molt  = str(valores[7]) # linear, não-linear ou mono-atômico
    dados = [] # lista para armazenar os resultados
#--------- comandos para tradução de interface de dados ----------------------
    E_eletronic = lang.eletronic
    ponto_zero = lang.point
    functions = lang.controle
#-----------------------------------------------------------------------------
    dados.append(f'''#{E_eletronic}      = {Eel:>30.6f} kJ/mol\n#{ponto_zero}   = {E_zpe:>30.6f} kJ/mol\n''')
    dados.append(f'\n#{functions}\n\n')
    st = ['# T(K)', 'U(kJ/mol)', 'S(kJ/mol*K)', 'H(kJ/mol)', 'G(kJ/mol)', 'A(kJ/mol)']
    dados.append(f"{st[0]:>7}{st[1]:>20}{st[2]:>20}{st[3]:>20}{st[4]:>20}{st[5]:>20}\n")

#------------------------------se sólido--------------------------------------
    if sist == 'solido':
        for i in arange(Tmin, Tmax+dT, dT):
            U = E_zpe + Eel + Evib(i, m)
            S = Svib(i, m)
            H = U
            G = H - i*S
            A = G
            dados.append(str(f"{i:>7.2f}{U:>20.6f}{S:>20.6f}{H:>20.6f}{G:>20.6f}{A:>20.6f}\n"))
        result = "".join(map(str,dados)) # retorna os dados para sistema sólido
#-----------------------------se molécula ------------------------------------
    elif sist == 'molecula':
#---------------------------se molécula linear--------------------------------
        if molt == 'linear':
            #------------------------centro de massa molécula linear----------
            cX, cY, cZ = 0, 0, 0 #
            for A, X, Y, Z in zip(label, x, y, z):
                cX, cY, cZ = cX+(atom[A]*X)/M, cY+(atom[A]*Y)/M, cZ+(atom[A]*Z)/M
            #-------------momento de inércia----------------------------------
            inercia = 0
            for A, X, Y, Z in zip(label, x, y, z): ## kg*angstrom^2 to kg*m^2
                dX, dY, dZ = ((X-cX)**2)*1e-20, ((Y-cY)**2)*1e-20, ((Z-cZ)**2)*1e-20
                inercia = inercia + atom[A]*(sqrt(dX+dY+dZ)**2)
            Trot = (h**2)/(2*inercia*k*4*(pi**2)) # temperatura rotacional
            # iterador para calcular as energias
            for i in arange(Tmin, Tmax+dT, dT):
                U = E_zpe + Eel + Evib(i, m) + Etrans(i) + Erot(i, molt) #E_interna
                S = Svib(i, m) + Strans(i, P, M) + Srot(i, Trot,0,0,0, sigma, molt)# entropia
                H = U + (k*i)/1000*N_A # entalpia
                G = H - i*S # gibbs
                A = U - i*S # helmholtz
                dados.append(str(f"{i:>7.2f}{U:>20.6f}{S:>20.6f}{H:>20.6f}{G:>20.6f}{A:>20.6f}\n"))
            result = "".join(map(str,dados))
#-----------------------------se molécula não linear--------------------------
        elif molt == 'nolinear':
            #------------------centro de massa molecula não linear------------
            cX, cY, cZ = 0, 0, 0 # centro de massa
            for A, X, Y, Z in zip(label, x, y, z):
                cX, cY, cZ = cX+(atom[A]*X), cY+(atom[A]*Y), cZ+(atom[A]*Z)
            cX, cY, cZ = cX/M, cY/M, cZ/M ### angstrom
            inerciaX = 0
            inerciaY = 0 # momentos de inércia
            inerciaZ = 0
            for A, X, Y, Z in zip(label, x, y, z): ## kg*angstrom^2 to kg*m^2
                dX, dY, dZ = ((X-cX)**2)*1e-20, ((Y-cY)**2)*1e-20, ((Z-cZ)**2)*1e-20
                inerciaX = inerciaX + atom[A]*(dY + dZ)
                inerciaY = inerciaY + atom[A]*(dX + dZ)
                inerciaZ = inerciaZ + atom[A]*(dX + dY)
            TrotX = (h**2)/(2*inerciaX*k*4*(pi**2))
            TrotY = (h**2)/(2*inerciaY*k*4*(pi**2))
            TrotZ = (h**2)/(2*inerciaZ*k*4*(pi**2))
            for i in arange(Tmin, Tmax+dT, dT):
                U = E_zpe + Eel + Evib(i, m) + Etrans(i) + Erot(i, molt)
                S = Svib(i, m) + Strans(i, P, M) + Srot(i, 0, TrotX, TrotY, TrotZ, sigma, molt)
                H = U + (k*i)/1000*N_A
                G = H - i*S
                A = U - i*S
                dados.append(str(f"{i:>7.2f}{U:>20.6f}{S:>20.6f}{H:>20.6f}{G:>20.6f}{A:>20.6f}\n"))
            result = "".join(map(str,dados))
#----------------------------se gás monoatômico-------------------------------
        elif molt =='atomo':
            for i in arange(Tmin, Tmax+dT, dT):
                U = E_zpe + Eel + Evib(i, m) + Etrans(i)
                S = Svib(i, m) + Strans(i, P, M)
                H = U + (k*i)/1000*N_A
                G = H - i*S
                A = U - i*S
                dados.append(str(f"{i:>7.2f}{U:>20.6f}{S:>20.6f}{H:>20.6f}{G:>20.6f}{A:>20.6f}\n"))
            result = "".join(map(str,dados))
    with open(path+'/temps/temp.nyp', 'w') as temp:
                temp.write(result)
    return result
