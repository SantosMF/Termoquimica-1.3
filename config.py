#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#     Módulo para computar as contribuições termodinâmicas
import os
path = os.path.dirname(os.path.realpath(__file__))
# passa a interface para o português
def Pt():
# interface
    with open (path+'/termoquimica.py', 'r') as entrada:
        string = entrada.read()
        l = string.replace('Idioma_gui_en', 'Idioma_gui_pt')
    with open(path+'/termoquimica.py', 'w') as arq: #cria os arquivos desejados
        arq.write(l)
# módulo
    with open (path+'/modulo.py', 'r') as entrada:
        string = entrada.read()
        l = string.replace('Idioma_gui_en', 'Idioma_gui_pt')
    with open(path+'/modulo.py', 'w') as arq: #cria os arquivos desejados
        arq.write(l)

### Passa a interface para o inglês
def En():
# interface
    with open (path+'/termoquimica.py', 'r') as entrada:
        string = entrada.read()
        l = string.replace('Idioma_gui_pt', 'Idioma_gui_en')
    with open(path+'/termoquimica.py', 'w') as arq: #cria os arquivos desejados
        arq.write(l)
# módulo
    with open (path+'/modulo.py', 'r') as entrada:
        string = entrada.read()
        l = string.replace('Idioma_gui_pt', 'Idioma_gui_en')
    with open(path+'/modulo.py', 'w') as arq: #cria os arquivos desejados
        arq.write(l)
