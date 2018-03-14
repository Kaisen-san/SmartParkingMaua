# importa bibliotecas necessarias
import os
from os.path import expanduser

# define local onde salvar as imagens
imgPath = expanduser("~") + "/SmartParkingMaua/images"


# cria diretorio onde as imagens serao salvas caso ele nao exista
if not os.path.exists(imgPath):
    os.makedirs(imgPath)


# Programa que busca o arquivo no path desejado
def Find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
