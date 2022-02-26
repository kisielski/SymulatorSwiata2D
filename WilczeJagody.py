import pygame
import os
from Roslina import Roslina

class WilczeJagody(Roslina):

	def __init__(self, x, y, swiat):
		self._Organizm__x = x
		self._Organizm__y = y
		self._Organizm__wiek = 0
		self._Organizm__sila = 99
		self._Organizm__inicjatywa = 0
		self._Organizm__typ = 'J'
		self._Organizm__swiat = swiat
		self._Organizm__img = pygame.image.load(os.path.join("assets", "wilczejagody.png"))
		swiat.dodajOrganizm(x, y, self)

	def porod(self, x, y):
		self._Organizm__swiat.dodajOrganizm(x, y, WilczeJagody(x, y, self._Organizm__swiat))