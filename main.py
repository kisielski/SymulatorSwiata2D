import pygame
import os
import time
import random
import math
from IO import IO
from Swiat import Swiat
from Ruchy import Ruchy
from Organizm import Organizm
from Trawa import Trawa
from Mlecz import Mlecz
from Guarana import Guarana
from WilczeJagody import WilczeJagody
from BarszczSosnowskiego import BarszczSosnowskiego
from Owca import Owca
from Wilk import Wilk
from Antylopa import Antylopa
from Lis import Lis
from Zolw import Zolw
from Cyberowca import Cyberowca
from Czlowiek import Czlowiek

GORA = 0
PRAWA = 1
DOL = 2
LEWA = 3

ROZMIAR_PLANSZY = 11
ROZMIAR_POLA = 64
SCIEZKA = "save.txt"

def main():
	run = True
	fps = 60
	clock = pygame.time.Clock()

	handler = IO()
	com = Ruchy()
	swiat = Swiat(ROZMIAR_PLANSZY, com)
	Czlowiek(5, 5, swiat)
	typy = ['T', 'M', 'G', 'J', 'B', 'O', 'W', 'A', 'L', 'Z', 'C']
	for typ in typy:
		utworzono = 0
		while utworzono < 3:
			x = random.randint(0, ROZMIAR_PLANSZY - 1)
			y = random.randint(0, ROZMIAR_PLANSZY - 1)
			if swiat.czyPustePole(x, y):
				IO.resp(swiat, x, y, typ)
				utworzono += 1
	while run:
		clock.tick(fps)
		swiat.rysujSwiat()
		if not swiat.wykonajTure(handler, run, SCIEZKA):
			run = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False



main()