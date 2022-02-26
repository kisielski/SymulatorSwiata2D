import pygame
import os
import random
from Zwierze import Zwierze

GORA = 0
PRAWA = 1
DOL = 2
LEWA = 3

class Antylopa(Zwierze):

	def __init__(self, x, y, swiat):
		self._Organizm__x = x
		self._Organizm__y = y
		self._Organizm__wiek = 0
		self._Organizm__sila = 3
		self._Organizm__inicjatywa = 7
		self._Organizm__typ = 'A'
		self._Organizm__swiat = swiat
		self._Organizm__img = pygame.image.load(os.path.join("assets", "antylopa.png"))
		swiat.dodajOrganizm(x, y, self)

	def akcja(self, com):
		pozycja = [self._Organizm__x, self._Organizm__y]
		kierunek = random.randint(GORA, LEWA)
		while not self.czyNaPlanszy(self._Organizm__swiat, pozycja, kierunek, 2):
			pozycja = [self._Organizm__x, self._Organizm__y]
			kierunek = random.randint(GORA, LEWA)
		if self._Organizm__swiat.czyPustePole(pozycja[0], pozycja[1]):
			self.przesun(pozycja[0], pozycja[1])
		else:
			self.kolizja(self._Organizm__swiat.getOrganizm(pozycja[0], pozycja[1]), com)
		self._Organizm__wiek += 1

	def porod(self, x, y):
		self._Organizm__swiat.dodajOrganizm(x, y, Antylopa(x, y, self._Organizm__swiat))