import pygame
import random
from Swiat import Swiat
from Ruchy import Ruchy
from Organizm import Organizm

GORA = 0
PRAWA = 1
DOL = 2
LEWA = 3

ROZMIAR_POLA = 64

class Zwierze(Organizm):

	def akcja(self, com):
		pozycja = [self._Organizm__x, self._Organizm__y]
		kierunek = random.randint(GORA, LEWA)
		while not self.czyNaPlanszy(self._Organizm__swiat, pozycja, kierunek, 1):
			pozycja = [self._Organizm__x, self._Organizm__y]
			kierunek = random.randint(GORA, LEWA)
		if self._Organizm__swiat.czyPustePole(pozycja[0], pozycja[1]):
			self.przesun(pozycja[0], pozycja[1])
		else:
			self.kolizja(self._Organizm__swiat.getOrganizm(pozycja[0], pozycja[1]), com)
		self._Organizm__wiek += 1


	def kolizja(self, org, com):
		if self._Organizm__typ == org._Organizm__typ and self._Organizm__typ != '*':
			if self._Organizm__wiek > 5 and org._Organizm__wiek > 5:
				pozycja = [org._Organizm__x, org._Organizm__y]
				jestMiejsce = False
				if self.czyNaPlanszy(self._Organizm__swiat, pozycja, GORA, 1) and self._Organizm__swiat.czyPustePole(pozycja[0], pozycja[1]):
					jestMiejsce = True
				else:
					pozycja = [org._Organizm__x, org._Organizm__y]
					if self.czyNaPlanszy(self._Organizm__swiat, pozycja, DOL, 1) and self._Organizm__swiat.czyPustePole(pozycja[0], pozycja[1]):
						jestMiejsce = True
				if jestMiejsce:
					info = f"{self._Organizm__typ} [{self._Organizm__x}, {self._Organizm__y}] rodzi nowy organizm {self._Organizm__typ}[{pozycja[0]}, {pozycja[1]}]"
					com.dodaj(info)
					self.porod(pozycja[0], pozycja[1])

		elif org._Organizm__typ == 'Z':
			if self._Organizm__sila >= 5:
				info = f"{self._Organizm__typ} [{self._Organizm__x}, {self._Organizm__y}] pokonuje {org._Organizm__typ} [{org._Organizm__x}, {org._Organizm__y}]"
				com.dodaj(info)
				self.przesun(org._Organizm__x, org._Organizm__y)
			else:
				info = f"{org._Organizm__typ} [{org._Organizm__x}, {org._Organizm__y}] odpiera {self._Organizm__typ} [{self._Organizm__x}, {self._Organizm__y}]"
				com.dodaj(info)

		elif org._Organizm__typ == 'A':
			szansa = random.randint(0, 1)
			if szansa == 0:
				uciekla = False
				kierunek = GORA
				while not uciekla and kierunek < 4:
					pozycja = [org._Organizm__x, org._Organizm__y]
					if self.czyNaPlanszy(self._Organizm__swiat, pozycja, kierunek, 1) and self._Organizm__swiat.czyPustePole(pozycja[0], pozycja[1]):
						info = f"{org._Organizm__typ} [{org._Organizm__x}, {org._Organizm__y}] ucieka przed {self._Organizm__typ} [{self._Organizm__x}, {self._Organizm__y}]"
						com.dodaj(info)
						org.przesun(pozycja[0], pozycja[1])
					else:
						kierunek += 1
			else:
				info = f"{self._Organizm__typ} [{self._Organizm__x}, {self._Organizm__y}] pokonuje {org._Organizm__typ} [{org._Organizm__x}, {org._Organizm__y}]"
				com.dodaj(info)
				self.przesun(org._Organizm__x, org._Organizm__y)

		elif org._Organizm__typ == 'G':
			info = f"{org._Organizm__typ} [{org._Organizm__x}, {org._Organizm__y}] wzmacnia {self._Organizm__typ} [{self._Organizm__x}, {self._Organizm__y}]"
			com.dodaj(info)
			self._Organizm__sila += 3
			self.przesun(org._Organizm__x, org._Organizm__y)

		else:
			if self._Organizm__sila > org._Organizm__sila:
				info = f"{self._Organizm__typ} [{self._Organizm__x}, {self._Organizm__y}] pokonuje {org._Organizm__typ} [{org._Organizm__x}, {org._Organizm__y}]"
				com.dodaj(info)
				self.przesun(org._Organizm__x, org._Organizm__y)
			elif self._Organizm__sila < org._Organizm__sila:
				info = f"{org._Organizm__typ} [{org._Organizm__x}, {org._Organizm__y}] pokonuje {self._Organizm__typ} [{self._Organizm__x}, {self._Organizm__y}]"
				com.dodaj(info)
				self._Organizm__swiat.wyczyscPole(self._Organizm__x, self._Organizm__y)
			else:
				if self._Organizm__wiek > org._Organizm__wiek:
					info = f"{self._Organizm__typ} [{self._Organizm__x}, {self._Organizm__y}] pokonuje {org._Organizm__typ} [{org._Organizm__x}, {org._Organizm__y}]"
					com.dodaj(info)
					self.przesun(org._Organizm__x, org._Organizm__y)
				elif self._Organizm__wiek < org._Organizm__wiek:
					info = f"{org._Organizm__typ} [{org._Organizm__x}, {org._Organizm__y}] pokonuje {self._Organizm__typ} [{self._Organizm__x}, {self._Organizm__y}]"
					com.dodaj(info)
					self._Organizm__swiat.wyczyscPole(self._Organizm__x, self._Organizm__y)
				else:
					pass


	def rysowanie(self, window):
		window.blit(self._Organizm__img, (ROZMIAR_POLA * self._Organizm__x, ROZMIAR_POLA * self._Organizm__y))


	def przesun(self, x, y):
		self._Organizm__swiat.wyczyscPole(self._Organizm__x, self._Organizm__y)
		self._Organizm__x = x
		self._Organizm__y = y
		self._Organizm__swiat.dodajOrganizm(x, y, self)
		self._Organizm__swiat.zajmijPole(x, y)


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