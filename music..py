import pygame
#inciar o mixer
pygame.mixer.init()
#iniciar o pygame
pygame.init()
pygame.mixer.music.load('00.mp3')
pygame.mixer.music.play(loops=0,start=0.0)
input()
pygame.event.wait()
