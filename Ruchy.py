import pygame

class Ruchy:

	def __init__(self):
		self.tekst = ""
		self.__ileInfo = 0

	def dodaj(self, ruch):
		self.tekst += ruch
		self.tekst += "; "
		self.__ileInfo += 1

	def wyczysc(self):
		self.tekst = ""
		self.__ileInfo = 0

	def getTekst(self):
		return self.tekst

	@property
	def ileInfo(self):
		return self._ileInfo
	