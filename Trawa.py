import pygame
import os
from Roslina import Roslina

class Trawa(Roslina):

	def __init__(self, x, y, swiat):
		self._Organizm__x = x
		self._Organizm__y = y
		self._Organizm__wiek = 0
		self._Organizm__sila = 0
		self._Organizm__inicjatywa = 0
		self._Organizm__typ = 'T'
		self._Organizm__swiat = swiat
		self._Organizm__img = pygame.image.load(os.path.join("assets", "trawa.png"))
		swiat.dodajOrganizm(x, y, self)

	def porod(self, x, y):
		self._Organizm__swiat.dodajOrganizm(x, y, Trawa(x, y, self._Organizm__swiat))