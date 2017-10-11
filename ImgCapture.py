# importa bibliotecas necessarias
import time
import RPi.GPIO as GPIO
import sys
import pygame.camera
import pygame.image
import os

# define local onde salvar as imagens
imgPath = "$HOME/SmartParkingMaua/images"

# cria diretorio onde as imagens serao salvas caso ele nao exista
if not os.path.exists(imgPath):
    os.makedirs(imgPath)

# inicializa camera
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0], (320,240)) # Investigate why image resolution is set to 176x144 instead of 320x240
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
def TakePicture(imgCount):
    # captura a imagem (eh necessario rodar o comando 3 vezes para poder capturar a imagem atual)
    img = cam.get_image()
    img = cam.get_image()
    img = cam.get_image()
    
    # define o nome da imagem de acordo com o numero do contador e a salva localmente
    imgName = imgPath + '/img_' + str(imgCount) + '.jpg'
    pygame.image.save(img, imgName)



# inicializa contador de fotos
imgCount = 0

try:
    while (1):
        # pega o valor no sensor de proximidade
        sensorValue = GetSensorValue()
        
        # compara com valor atual do sensor com a distancia minima definida
        if (sensorValue < minDist):
            # mostra a distancia atual do sensor
            #print("Distance: {0:.2f}".format(triggerValue))
            
            # incrementa o contador de fotos e realiza captura da imagem 
            imgCount += 1
            TakePicture(imgCount)
            
            # nao captura novas imagens enquanto o valor atual do sensor for menor que a distancia minida definida
            while (sensorValue < minDist):
                # compara com valor atual do sensor com a distancia minima definida
                sensorValue = GetSensorValue()
                
# Pausa a execucao do while quando pressionamos CTRL-C
except KeyboardInterrupt:
    pass

