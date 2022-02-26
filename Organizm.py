from abc import ABC, abstractmethod

class Organizm:

	@property
	def typ(self):
	    return self.__typ

	@property
	def sila(self):
	    return self.__sila

	@property
	def wiek(self):
	    return self.__wiek

	@property
	def inicjatywa(self):
	    return self.__inicjatywa

	@property
	def x(self):
	    return self.__x

	@property
	def y(self):
	    return self.__y

	@property
	def swiat(self):
	    return self.__swiat

	@property
	def img(self):
	    return self.__img

	@abstractmethod
	def akcja(self, com):
		pass

	@abstractmethod
	def kolizja(self, org, com):
		pass

	@abstractmethod
	def rysowanie(self, window):
		pass

	@abstractmethod
	def porod(self, x, y):
		pass