#tocando mp3

#pip install pygame

import pygame
import time
import os

# Pega a pasta onde o script está localizado
pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_mp3 = os.path.join(pasta_atual, "ex021.mp3")

# Inicializa o mixer de áudio
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load(caminho_mp3)

# Toca a música
pygame.mixer.music.play()

# Mantém o programa rodando enquanto a música toca
while pygame.mixer.music.get_busy():
    time.sleep(1)