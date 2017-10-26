# importa bibliotecas necessarias
import time
import RPi.GPIO as GPIO
import sys
import pygame.camera
import pygame.image
from commonFunctions import *


# inicializa camera
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0], (176,144)) # Investigate why image resolution is set to 176x144 instead of 320x240
cam.start()


# inicializa a distancia minima
minDist = 60


# Funcao que retorna o valor do sensor de proximidade
def GetSensorValue():
    GPIO.setmode(GPIO.BCM)

    # gpio 23
    ECHO_PIN = 23

    # gpio 24
    TRIG_PIN = 24

    # Velocidade do som 340,29 m/s -&gt; 34029 cm/s
    SPEED_OF_SOUND = 34029

    # configura os pinos
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)

    GPIO.output(TRIG_PIN, GPIO.LOW)
    time.sleep(1)

    # emite o sinal com duração de 10us, marcando o inicio da medição
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, GPIO.LOW)

    # Nosso primeiro passo deve ser o de gravar o ultimo baixo timestamp (time_start) para o ECHO (início de pulso), pouco antes do sinal de retorno.
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        time_start = time.time()

    # Uma vez que um sinal é recebido, o valor é alterado a partir de baixo (LOW) e alta (HIGH), e o sinal irá permanecer elevada durante a duração do impulso de eco. portanto, precisamos também da última alta timestamp para o ECHO (time_end).
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        time_end = time.time()

    # calculamos a diferença de tempo
    time_elapsed = time_end - time_start

    # calcula a distancia em cm, como tempos o comprimento da ida e volta do sinal, e necessario a divisão por 2, pois queremos a distancia do ultrasônico até o objeto.
    distance = (time_elapsed * SPEED_OF_SOUND) / 2

    GPIO.cleanup()

    return distance


# Funcao que captura e salva a imagem da camera
def TakePicture(imgName):
    # captura a imagem (eh necessario rodar o comando 3 vezes para poder capturar a imagem atual)
    img = cam.get_image()
    img = cam.get_image()
    img = cam.get_image()
    
    # define o nome da imagem de acordo com o numero do contador e a salva localmente
    imgFullPath = imgPath + '/' + imgName
    pygame.image.save(img, imgFullPath)


# programa que realiza a captura da imagem apos um trigger do sensor
def CaptureImg():
    while (1):
        # inicializa/retorna o contador pra 1, uma vez que as imagens sao deletas conforme são classificadas
        imgCount=1
            
        # pega o valor no sensor de proximidade
        sensorValue = GetSensorValue()	
		
        # define nome da imagem
        imgName = "img_" + str(imgCount) + ".jpg"
		
        # compara com valor atual do sensor com a distancia minima definida
        if (sensorValue < minDist):
            
            # procura pelo nome de imagem disponivel mais proximo
            while(Find(imgName, imgPath) != None):
                imgCount+=1
                imgName = "img_" + str(imgCount) + ".jpg"

            # captura e salva a imagem
            TakePicture(imgName)
            
            #print(imgName) # imprimi nome da imagem capturada
 
            # nao captura novas imagens enquanto o valor atual do sensor for menor que a distancia minida definida
            while (sensorValue < minDist):
                # compara com valor atual do sensor com a distancia minima definida
                sensorValue = GetSensorValue()


if (__name__ == '__main__'):
    CaptureImg()
