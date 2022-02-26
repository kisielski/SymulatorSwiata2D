import pygame
import os
from Zwierze import Zwierze

GORA = 0
PRAWA = 1
DOL = 2
LEWA = 3

class Cyberowca(Zwierze):

	def __init__(self, x, y, swiat):
		self._Organizm__x = x
		self._Organizm__y = y
		self._Organizm__wiek = 0
		self._Organizm__sila = 11
		self._Organizm__inicjatywa = 7
		self._Organizm__typ = 'C'
		self._Organizm__swiat = swiat
		self._Organizm__img = pygame.image.load(os.path.join("assets", "cyberowca.png"))
		swiat.dodajOrganizm(x, y, self)

	def akcja(self, com):
		pozycja = self._Organizm__swiat.najblizszyBarszcz(self._Organizm__x, self._Organizm__y)
		if pozycja != -1:
			ruch = [self._Organizm__x, self._Organizm__y]
			if ruch[0] < pozycja[0]:
				ruch[0] += 1
				if self._Organizm__swiat.czyPustePole(ruch[0], ruch[1]):
					self.przesun(ruch[0], ruch[1])
				else:
					self.kolizja(self._Organizm__swiat.getOrganizm(ruch[0], ruch[1]), com)
			elif ruch[0] > pozycja[0]:
				ruch[0] -= 1
				if self._Organizm__swiat.czyPustePole(ruch[0], ruch[1]):
					self.przesun(ruch[0], ruch[1])
				else:
					self.kolizja(self._Organizm__swiat.getOrganizm(ruch[0], ruch[1]), com)
			elif ruch[1] < pozycja[1]:
				ruch[1] += 1
				if self._Organizm__swiat.czyPustePole(ruch[0], ruch[1]):
					self.przesun(ruch[0], ruch[1])
				else:
					self.kolizja(self._Organizm__swiat.getOrganizm(ruch[0], ruch[1]), com)
			elif ruch[1] > pozycja[1]:
				ruch[1] -= 1
				if self._Organizm__swiat.czyPustePole(ruch[0], ruch[1]):
					self.przesun(ruch[0], ruch[1])
				else:
					self.kolizja(self._Organizm__swiat.getOrganizm(ruch[0], ruch[1]), com)
		else:
			super().akcja(com)

	def porod(self, x, y):
		self._Organizm__swiat.dodajOrganizm(x, y, Cyberowca(x, y, self._Organizm__swiat))