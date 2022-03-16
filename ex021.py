import pygame

a = float(input('tempo da música: '))

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('../Arquivos para exercício/ex021.mp3')
pygame.mixer.music.play(loops=0, start=a)
pygame.event.wait()

