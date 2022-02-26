import pygame
import os
import math
from IO import IO
from Organizm import Organizm
from Zwierze import Zwierze

GORA = 0
PRAWA = 1
DOL = 2
LEWA = 3
ROZMIAR_POLA = 64

class Czlowiek(Zwierze):

	def __init__(self, x, y, swiat):
		self.__umiejetnosc = 0
		self.__cooldown = 0
		self._Organizm__x = x
		self._Organizm__y = y
		self._Organizm__wiek = 0
		self._Organizm__sila = 5
		self._Organizm__inicjatywa = 4
		self._Organizm__typ = '*'
		self._Organizm__swiat = swiat
		self._Organizm__img = pygame.image.load(os.path.join("assets", "gracz.png"))
		swiat.dodajOrganizm(x, y, self)

	def akcja(self, handler, sciezka, com):
		wykonanoRuch = False
		czyNowyOrganizm = False
		while not wykonanoRuch:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						kierunek = GORA
					elif event.key == pygame.K_RIGHT:
						kierunek = PRAWA
					elif event.key == pygame.K_DOWN:
						kierunek = DOL
					elif event.key == pygame.K_LEFT:
						kierunek = LEWA
					elif event.key == pygame.K_x:
						kierunek = 4
					wykonanoRuch = True
					if event.key == pygame.K_o:
						handler.odczyt(self._Organizm__swiat, sciezka, com, self)
						self._Organizm__swiat.rysujSwiat()
						wykonanoRuch = False
					elif event.key == pygame.K_s:
						handler.zapis(self._Organizm__swiat, sciezka, com)
						self._Organizm__swiat.rysujSwiat()
						wykonanoRuch = False
				elif event.type == pygame.MOUSEBUTTONDOWN:
					self.stworzOrganizm(self._Organizm__swiat, pygame.mouse.get_pos())
					self._Organizm__swiat.rysujSwiat()
				elif event.type == pygame.QUIT:
					return False

		if self.__cooldown > 0:
			self.__cooldown -= 1
		if self.__cooldown >= 5:
			self._Organizm__sila -= 1
		pozycja = [self._Organizm__x, self._Organizm__y]
		spec = False
		if kierunek == 4:
			spec = self.specjalnaUmiejetnosc()
			if not spec:
				info = f"Nie możesz użyć umiejętności, odczekaj {self.__cooldown} rund"
				com. dodaj(info)
				self._Organizm__swiat.rysujSwiat()
				while kierunek < 0 or kierunek > 3:
					for event in pygame.event.get():
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_UP:
								kierunek = GORA
							elif event.key == pygame.K_RIGHT:
								kierunek = PRAWA
							elif event.key == pygame.K_DOWN:
								kierunek = DOL
							elif event.key == pygame.K_LEFT:
								kierunek = LEWA	
		if spec:
			info = f"Gracz użył specjalnej umiejętności, jego siła wynosi teraz {self._Organizm__sila}"
			com.dodaj(info)
		else:
			while not self.czyNaPlanszy(self._Organizm__swiat, pozycja, kierunek, 1):
				pozycja = [self._Organizm__x, self._Organizm__y]
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_UP:
							pozycja[1] -= 1
						elif event.key == pygame.K_RIGHT:
							pozycja[0] += 1
						elif event.key == pygame.K_DOWN:
							pozycja[1] += 1
						elif event.key == pygame.K_LEFT:
							pozycja[0] -= 1					

		if self._Organizm__swiat.czyPustePole(pozycja[0], pozycja[1]):
			self.przesun(pozycja[0], pozycja[1])
		else:
			self.kolizja(self._Organizm__swiat.getOrganizm(pozycja[0], pozycja[1]), com)
		self._Organizm__wiek += 1
		return True

	def specjalnaUmiejetnosc(self):
		if self.__cooldown == 0:
			self.__cooldown = 10
			self._Organizm__sila += 5
			return True
		return False

	def stworzOrganizm(self, swiat, pos):
		x = math.floor(pos[0] / ROZMIAR_POLA)
		y = math.floor(pos[1] / ROZMIAR_POLA)
		typ = self._Organizm__swiat.rysujWybor()
		IO.resp(swiat, x, y, typ)

	@property
	def cooldown(self):
		return self.__cooldown
