import pygame
import os
from Zwierze import Zwierze

class Wilk(Zwierze):

	def __init__(self, x, y, swiat):
		self._Organizm__x = x
		self._Organizm__y = y
		self._Organizm__wiek = 0
		self._Organizm__sila = 9
		self._Organizm__inicjatywa = 5
		self._Organizm__typ = 'W'
		self._Organizm__swiat = swiat
		self._Organizm__img = pygame.image.load(os.path.join("assets", "wilk.png"))
		swiat.dodajOrganizm(x, y, self)

	def porod(self, x, y):
		self._Organizm__swiat.dodajOrganizm(x, y, Wilk(x, y, self._Organizm__swiat))