import pygame
import random
from Swiat import Swiat
from Organizm import Organizm

GORA = 0
PRAWA = 1
DOL = 2
LEWA = 3

ROZMIAR_POLA = 64

class Roslina(Organizm):

	def akcja(self, com):
		szansa = random.randint(1, 100)
		if szansa == 100:
			jestMiejsce = False
			kierunek = random.randint(0, 3)
			proba = 0
			while not jestMiejsce and proba < 4:
				pozycja = [self._Organizm__x, self._Organizm__y]
				if self.czyNaPlanszy(self._Organizm__swiat, pozycja, kierunek, 1) and self._Organizm__swiat.czyPustePole(pozycja[0], pozycja[1]):
					jestMiejsce = True
				else:
					kierunek += 1
					kierunek %= 4
					proba += 1
			if jestMiejsce:
				info = f"{self._Organizm__typ} [{self._Organizm__x}, {self._Organizm__y}] rodzi nowy organizm {self._Organizm__typ}[{pozycja[0]}, {pozycja[1]}]"
				com.dodaj(info)
				self.porod(pozycja[0], pozycja[1])

	def rysowanie(self, window):
		window.blit(self._Organizm__img, (ROZMIAR_POLA * self._Organizm__x, ROZMIAR_POLA * self._Organizm__y))

	def kolizja(self, org, com):
		pass


	@staticmethod
	def czyNaPlanszy(swiat, pozycja, kierunek, odleglosc):
		rozmiar = swiat.rozmiar
		x, y = pozycja[0], pozycja[1]
		prawidlowePole = False
		if kierunek == GORA:
			if y - odleglosc >= 0:
				y -= odleglosc
				prawidlowePole = True
		elif kierunek == PRAWA:
			if x + odleglosc < rozmiar:
				x += odleglosc
				prawidlowePole = True
		elif kierunek == DOL:
			if y + odleglosc < rozmiar:
				y += odleglosc
				prawidlowePole = True
		elif kierunek == LEWA:
			if x - odleglosc >= 0:
				x -= 1
				prawidlowePole = True
		pozycja[0], pozycja[1] = x, y
		return prawidlowePole