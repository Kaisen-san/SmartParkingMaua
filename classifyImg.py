# importa bibliotecas necessarias
import time
import os
import tensorflow as tf
from multiprocessing import Process
from classifier import *
from commonFunctions import *


def ClassifyImg():
    while(1):
        # inicializa/retorna o contador pra 1, uma vez que as imagens sao deletas conforme são classificadas
        imgCount=1

        # define nome da imagem
        imgName = "img_" + str(imgCount) + ".jpg"

        # define caminho completo da imagem
        imgFullPath = imgPath + '/' + imgName

        # classifica as imagens enquanto houver
        while(Find(imgName, imgPath) != None):
            # declaracao do processo de classificacao de imagem
            p = Process(target=Classify, args=(imgFullPath,))

            # inicia o processo de classificacao de imagem
            p.start()

            # trava o processo de classicacao de imagem enquanto ele estiver ativo
            while(p.is_alive() == 1):
                time.sleep(1)

            # finaliza o processo de classificacao de imagem
            p.terminate()

            # deleta a imagem classificada
            os.remove(imgFullPath)

            # imprimi nome da imagem classificada/removida
            print("Classified/Deleted image name:" + imgName)

            # atualiza as variaveis utilizadas
            imgCount+=1
            imgName = "img_" + str(imgCount) + ".jpg"
            imgFullPath = imgPath + '/' + imgName

            # Linha em branco no log
            print()

if (__name__ == '__main__'):
    ClassifyImg()
