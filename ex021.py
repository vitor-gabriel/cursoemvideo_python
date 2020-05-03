import pygame, sys
from pygame.locals import *
import os

os.environ['SDL_AUDIODRIVER'] = 'dsp'

pygame.mixer.init()

pygame.mixer.music.load('ex021.mp3')

pygame.mixer.music.play()
pygame.event.wait()