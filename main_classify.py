# importa bibliotecas necessarias
import time
import sys
import os
from os.path import expanduser
import tensorflow as tf
from multiprocessing import Process
from label_image import *

# define local onde salvar as imagens
imgPath = expanduser("~") + "/SmartParkingMaua/images"
print(imgPath)

# cria diretorio onde as imagens serao salvas caso ele nao exista
if not os.path.exists(imgPath):
    os.makedirs(imgPath)

# Programa que busca o arquivo no path desejado
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

# Programa que classifica a imagem na fila e a deleta apos o tratamento
def classifyImg():
    print("classifyImg in")
    imgCount=1
    while(1):
        imgName = "img_" + str(imgCount) + ".jpg"
        if (find(imgName, imgPath) != None):
            imgFullPath = imgPath + '/' + imgName
            classify(imgFullPath)
            os.remove(imgFullPath)
            imgCount+=1
        else:
            imgCount=1
            time.sleep(1)


if (__name__ == '__main__'):
    classifyImg()


