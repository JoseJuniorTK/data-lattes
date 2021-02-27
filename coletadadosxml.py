# -*- coding: utf-8 -*-
"""coletadadosxml.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sIhLFvEeXfq4op5aw5jaMUCxnBxdztgB
"""

import xml.etree.ElementTree as ET
import os
import glob
#tree = ET.parse('.\CurriculosXML')
#root = tree.getroot()

#Variáveis a serem levadas em conta para plotagem dos gráficos:
#PRODUÇÕES BIBLIOGRÁFICAS (GRÁFICO 1):
#1 - Artigos publicados (ano e total)
#2 - Capítulos de livros (ano e total)
#3 - Trabalho em eventos (ano e total)
#4 - Livros (ano e total)
#5 - Textos em jornais ou revistas (ano e total)
#6 - Artigos aceitos para publicação (ano e total)

#PRODUÇÕES BIBLIOGRÁFICAS COM DOI (GRÁFICO 2):
#1 - Artigos publicados (ano e total)
#2 - Capítulos de livros (ano e total)
#3 - Trabalho em eventos (ano e total)
#4 - Livros (ano e total)
#5 - Artigos aceitos para publicação (ano e total)

#ORIENTAÇÕES CONCLUÍDAS (GRÁFICO 3):
#Mestrado (ano e total)
#Doutorado (ano e total)
#Pós-Doutorado (ano e total)
#Outras (ano e total)

#Cria um lista dos anos dos trabalhos em eventos com seus respectivos DOIs
#Argumento é a ID do professor
def trab_eventos(id):
    lista = []
    for i in range(0, len(curriculos)):
        tree = ET.parse(curriculos[i])
        root = tree.getroot()
        for j in root.iter('CURRICULO-VITAE'):   
            if str(j.attrib['NUMERO-IDENTIFICADOR']) == id:
                    for l in root.iter('DADOS-BASICOS-DO-TRABALHO'):
                        ano = l.attrib['ANO-DO-TRABALHO']
                        doi = l.attrib['DOI']
                        lista.append([ano,doi])

    return lista

#Cria um lista dos anos dos trabalhos em eventos com seus respectivos DOIs
#Argumento é a ID do professor
def art_publicados(id):
    lista = []
    for i in range(0, len(curriculos)):
        tree = ET.parse(curriculos[i])
        root = tree.getroot()
        for j in root.iter('CURRICULO-VITAE'):   
            if str(j.attrib['NUMERO-IDENTIFICADOR']) == id:
                for k in root.iter('DADOS-BASICOS-DO-ARTIGO'): 
                    ano = k.attrib['ANO-DO-ARTIGO']
                    doi = k.attrib['DOI']
                    lista.append([ano,doi])
    return lista

#Cria um lista dos anos dos capitulos publicados com seus respectivos DOIs
#Argumento é a ID do professor
def cap_publicados(id):
    lista = []
    for i in range(0, len(curriculos)):
        tree = ET.parse(curriculos[i])
        root = tree.getroot()
        for j in root.iter('CURRICULO-VITAE'):   
            if str(j.attrib['NUMERO-IDENTIFICADOR']) == id:
                for k in root.iter('DADOS-BASICOS-DO-CAPITULO'): 
                    ano = k.attrib['ANO']
                    doi = k.attrib['DOI']
                    lista.append([ano,doi])
    return lista

#Cria um lista dos anos dos livros publicados com seus respectivos DOIs
#Argumento é a ID do professor
def livros_publicados(id):
    lista = []
    for i in range(0, len(curriculos)):
        tree = ET.parse(curriculos[i])
        root = tree.getroot()
        for j in root.iter('CURRICULO-VITAE'):   
            if str(j.attrib['NUMERO-IDENTIFICADOR']) == id:
                for k in root.iter('DADOS-BASICOS-DO-LIVRO'): 
                    ano = k.attrib['ANO']
                    doi = k.attrib['DOI']
                    lista.append([ano,doi])
    return lista

#Cria um lista dos anos demais produções bibliográficas com seus respectivos DOIs
#Argumento é a ID do professor
def demais_prod_bib(id):
    lista = []
    for i in range(0, len(curriculos)):
        tree = ET.parse(curriculos[i])
        root = tree.getroot()
        for j in root.iter('CURRICULO-VITAE'):   
            if str(j.attrib['NUMERO-IDENTIFICADOR']) == id:
                for k in root.iter('DADOS-BASICOS-DE-OUTRA-PRODUCAO'): 
                    ano = k.attrib['ANO']
                    doi = k.attrib['DOI']
                    lista.append([ano,doi])
    return lista

#Cria um lista dos anos das outras orientações concluídas
#Argumento é a ID do professor
def outras_orient_conc(id):
    lista = []
    for i in range(0, len(curriculos)):
        tree = ET.parse(curriculos[i])
        root = tree.getroot()
        for j in root.iter('CURRICULO-VITAE'):   
            if str(j.attrib['NUMERO-IDENTIFICADOR']) == id:
                for k in root.iter('DADOS-BASICOS-DE-OUTRAS-ORIENTACOES-CONCLUIDAS'): 
                    ano = k.attrib['ANO']
                    lista.append([ano])
    return lista

#Cria um lista dos anos das orientações de mestrado concluídas com seus respectivos DOIs
#Argumento é a ID do professor
def orient_mestrado_conc(id):
    lista = []
    for i in range(0, len(curriculos)):
        tree = ET.parse(curriculos[i])
        root = tree.getroot()
        for j in root.iter('CURRICULO-VITAE'):   
            if str(j.attrib['NUMERO-IDENTIFICADOR']) == id:
                for k in root.iter('DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-MESTRADO'): 
                    ano = k.attrib['ANO']
                    lista.append([ano])
    return lista

#Cria um lista dos anos das orientações de doutorado concluídas com seus respectivos DOIs
#Argumento é a ID do professor
def orient_doutorado_conc(id):
    lista = []
    for i in range(0, len(curriculos)):
        tree = ET.parse(curriculos[i])
        root = tree.getroot()
        for j in root.iter('CURRICULO-VITAE'):   
            if str(j.attrib['NUMERO-IDENTIFICADOR']) == id:
                for k in root.iter('DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-DOUTORADO'): 
                    ano = k.attrib['ANO']
                    lista.append([ano])
    return lista

#Cria um lista dos anos das orientações de pós-doutorado concluídas com seus respectivos DOIs
#Argumento é a ID do professor
def orient_posdoc_conc(id):
    lista = []
    for i in range(0, len(curriculos)):
        tree = ET.parse(curriculos[i])
        root = tree.getroot()
        for j in root.iter('CURRICULO-VITAE'):   
            if str(j.attrib['NUMERO-IDENTIFICADOR']) == id:
                for k in root.iter('DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-POS-DOUTORADO'): 
                    ano = k.attrib['ANO']
                    lista.append([ano])
    return lista

cont = 0
curriculos = []
for f in glob.glob('CurriculosXML/*'):    #Lista os arquivos xml da pasta
    curriculos.append(f)
    cont = cont+1

#Cria uma lista dos nomes dos professores com seus respectivos IDS do Lattes
professor = []
for i in range(0, len(curriculos)):
    tree = ET.parse(curriculos[i])
    root = tree.getroot()
    for j in root.iter('CURRICULO-VITAE'):   
        id = str(j.attrib['NUMERO-IDENTIFICADOR'])
        for k in root.iter('DADOS-GERAIS'):   
          nome_professor = str(k.attrib['NOME-COMPLETO']).upper()
          professor.append([id,nome_professor])

print(professor)

#Usando alguma id da lista professor, no exemplo: prof. Lídio
trabEventos = []
artPub = []
capPub = []
livrosPub = []
demaisProd = []
outrasOrient = []
orientMest = []
orientDoc = []
orientPDoc = []

print('TRABALHOS EM EVENTOS')
trabEventos = trab_eventos('0970111009687779')
print(f'Lista: {trabEventos}')
print(f'Total: {len(trabEventos)}')
print('\n')

print('ARTIGOS PUBLICADOS')
artPub = art_publicados('0970111009687779')
print(f'Lista: {artPub}')
print(f'Total: {len(artPub)}')
print('\n')

print('CAPITULOS PUBLICADOS')
capPub = cap_publicados('0970111009687779')
print(f'Lista: {capPub}')
print(f'Total: {len(capPub)}')
print('\n')

print('LIVROS PUBLICADOS')
livrosPub = livros_publicados('0970111009687779')
print(f'Lista: {livrosPub}')
print(f'Total: {len(livrosPub)}')
print('\n')

print('DEMAIS PRODUÇÕES BIBLIOGRÁFICAS')
demaisProd = demais_prod_bib('0970111009687779')
print(f'Lista: {demaisProd}')
print(f'Total: {len(demaisProd)}')
print('\n')

print('OUTRAS ORIENTAÇÕES')
outrasOrient = outras_orient_conc('0970111009687779')
print(f'Lista: {outrasOrient}')
print(f'Total: {len(outrasOrient)}')
print('\n')

print('ORIENTAÇÕES MESTRADO CONCLUÍDAS') 
orientMest = orient_mestrado_conc('0970111009687779')
print(f'Lista: {orientMest}')
print(f'Total: {len(orientMest)}')
print('\n')

print('ORIENTAÇÕES DOUTORADO CONCLUÍDAS')
orientDoc = orient_doutorado_conc('0970111009687779')
print(f'Lista: {orientDoc}')
print(f'Total: {len(orientDoc)}')
print('\n')

print('ORIENTAÇÕES PÓS-DOUTORADO CONCLUÍDAS') 
orientPDoc = orient_posdoc_conc('0970111009687779')
print(f'Lista: {orientPDoc}')
print(f'Total: {len(orientPDoc)}')