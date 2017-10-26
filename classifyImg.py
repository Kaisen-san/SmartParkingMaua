# importa bibliotecas necessarias
import time
import os
import tensorflow as tf
from multiprocessing import Process
from label_image import *
from commonFunctions import *


# programa que classifica a imagem na fila e a deleta apos o tratamento
def ClassifyImg():   
    while(1):
        # inicializa/retorna o contador pra 1, uma vez que as imagens sao deletas conforme são classificadas
        imgCount=1
        
        # define nome da imagem
        imgName = "img_" + str(imgCount) + ".jpg"
        
        # classifica as imagens enquanto houver, e deleta as que foram classificadas
        while(Find(imgName, imgPath) != None):
            imgFullPath = imgPath + '/' + imgName
            Classify(imgFullPath)
            os.remove(imgFullPath)
            #print(imgName) # imprimi nome da imagem classificada/removida
            imgCount+=1
            imgName = "img_" + str(imgCount) + ".jpg"
            time.sleep(20) # intervalo entre cada classificacao


if (__name__ == '__main__'):
    ClassifyImg()
