import pygame
import os
from Roslina import Roslina

class BarszczSosnowskiego(Roslina):

	def __init__(self, x, y, swiat):
		self._Organizm__x = x
		self._Organizm__y = y
		self._Organizm__wiek = 0
		self._Organizm__sila = 10
		self._Organizm__inicjatywa = 0
		self._Organizm__typ = 'B'
		self._Organizm__swiat = swiat
		self._Organizm__img = pygame.image.load(os.path.join("assets", "barszczsosnowskiego.png"))
		swiat.dodajOrganizm(x, y, self)

	def porod(self, x, y):
		self._Organizm__swiat.dodajOrganizm(x, y, BarszczSosnowskiego(x, y, self._Organizm__swiat))

	def akcja(self, com):
		x, y = self._Organizm__x - 1, self._Organizm__y - 1
		zasiegX, zasiegY = 3, 3
		if x < 0:
			x += 1
			zasiegX -= 1
		if y < 0:
			y += 1
			zasiegY -= 1
		for i in range(zasiegX):
			for j in range(zasiegY):
				if i != 1 or j != 1:
					if (x + i) < self._Organizm__swiat.rozmiar and (y + j) < self._Organizm__swiat.rozmiar:
						if not self._Organizm__swiat.czyPustePole(x + i, y + j):
							org = self._Organizm__swiat.getOrganizm((x + i), (y + j))
							typ = org.typ
							if typ == 'O' or typ == 'W' or typ == 'A' or typ == 'Z' or typ == 'L' or typ == '*':
								info = f"{self._Organizm__typ} [{self._Organizm__x}, {self._Organizm__y}] zabija {typ}[{org._Organizm__x}, {org._Organizm__y}]"
								com.dodaj(info)
								self._Organizm__swiat.wyczyscPole(x + i, y + j)
		super().akcja(com)