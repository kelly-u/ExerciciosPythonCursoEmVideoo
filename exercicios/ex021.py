# Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.

from pygame import mixer

mixer.init()
mixer.music.load('C:/Users/gleic/Downloads/Bento e Totó - O Patinho Colorido (Desenho Infantil).mp3')
mixer.music.play()
while mixer.music.get_busy():
    continue

quit()
