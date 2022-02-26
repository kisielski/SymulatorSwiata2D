import pygame
import os
import math
from Organizm import Organizm
pygame.font.init()

GORA = 0
PRAWA = 1
DOL = 2
LEWA = 3

MAX_INICJATYWA = 7

ILE_ROZNYCH_TYPOW = 11
ROZMIAR_POLA = 64
ROZMIAR_CZCIONKI = 16
CZCIONKA = pygame.font.SysFont("arial", ROZMIAR_CZCIONKI)
WIDTH, HEIGHT, TEKST = 704, 704, 100
WINDOW = pygame.display.set_mode((WIDTH, (HEIGHT + TEKST)))
pygame.display.set_caption("Symulator Swiata, Krzysztof Szymankiewicz, 183216")

TLO = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tlo.png")), (WIDTH, (HEIGHT + TEKST)))

class Swiat:
	def __init__(self, rozmiar, com):
		if rozmiar > 0:
			self.__rozmiar = rozmiar
			self.com = com
			self.__zajetePola = [[] for i in range(rozmiar)]
			self.__organizmy = [[] for i in range(rozmiar)]
			for i in range(rozmiar):
				for j in range(rozmiar):
					self.__zajetePola[i].append(0)
					self.__organizmy[i].append(0)
		else:
			return 1

	def rysujSwiat(self):
		ile = 0
		WINDOW.blit(TLO, (0, 0))
		for i in range(self.__rozmiar):
			for j in range(self.__rozmiar):
				if self.__zajetePola[i][j] != 0:
					self.__organizmy[i][j].rysowanie(WINDOW)
		for info in self.com.getTekst().split("; "):
			tekst = CZCIONKA.render(info, 1, (0, 0, 0))
			WINDOW.blit(tekst, (0, HEIGHT + ile * ROZMIAR_CZCIONKI))
			ile += 1
		pygame.display.update()

	def wyczyscPole(self, x, y):
		self.__zajetePola[x][y] = 0

	def dodajOrganizm(self, x, y, org):
		self.__zajetePola[x][y] = 1
		self.__organizmy[x][y] = org

	def wykonajTure(self, handler, run, sciezka):
		inicjatywa = MAX_INICJATYWA
		graczZyje = False
		for i in range(self.__rozmiar):
				for j in range(self.__rozmiar):
					if self.__zajetePola[i][j] == 1:
						if self.__organizmy[i][j].typ == '*':
							graczZyje = True
		if not graczZyje:
			self.com.wyczysc()
		while inicjatywa >= 0:
			for i in range(self.__rozmiar):
				for j in range(self.__rozmiar):
					if self.__zajetePola[i][j] == 1:
						if self.__organizmy[i][j].inicjatywa == inicjatywa:
							if self.__organizmy[i][j].typ == '*':
								self.rysujSwiat()
								self.com.wyczysc()
								if not self.__organizmy[i][j].akcja(handler, sciezka, self.com):
									return False
							else:
								self.__organizmy[i][j].akcja(self.com)
			inicjatywa -= 1
		for i in range(self.__rozmiar):
			for j in range(self.__rozmiar):
				if self.__zajetePola[i][j] == 2:
					self.__zajetePola[i][j] = 1
		self.rysujSwiat()
		return True

	def najblizszyBarszcz(self, x, y):
		zasieg = 1
		startX, koniecX = x - 1, x + 1
		startY, koniecY = y - 1, y + 1
		while zasieg < self.__rozmiar:
			for i in range(startX, koniecX):
				for j in range(startY, koniecY):
					if self.__zajetePola[i][j] == 1:
						if self.__organizmy[i][j].typ == 'B':
							pozycja = [i, j]
							return pozycja
			zasieg += 1
			startX -= 1
			startY -= 1
			koniecX += 1
			koniecY += 1
			if startX < 0:
				startX = 0
			if koniecX > self.__rozmiar:
				koniecX = self.__rozmiar
			if startY < 0:
				startY = 0
			if koniecY > self.__rozmiar:
				koniecY = self.__rozmiar
		return -1

	def czyPustePole(self, x, y):
		if self.__zajetePola[x][y] == 0:
			return True
		else:
			return False

	@staticmethod
	def rysujWybor():
		winPos = [0, HEIGHT]
		typy = [pygame.image.load(os.path.join("assets", "trawa.png")),
		 pygame.image.load(os.path.join("assets", "mlecz.png")),
		 pygame.image.load(os.path.join("assets", "guarana.png")),
		 pygame.image.load(os.path.join("assets", "wilczejagody.png")),
		 pygame.image.load(os.path.join("assets", "barszczsosnowskiego.png")),
		 pygame.image.load(os.path.join("assets", "owca.png")),
		 pygame.image.load(os.path.join("assets", "wilk.png")),
		 pygame.image.load(os.path.join("assets", "antylopa.png")),
		 pygame.image.load(os.path.join("assets", "lis.png")),
		 pygame.image.load(os.path.join("assets", "zolw.png")),
		 pygame.image.load(os.path.join("assets", "cyberowca.png"))]

		typyChar = ['T', 'M', 'G', 'J', 'B', 'O', 'W', 'A', 'L', 'Z', 'C']
		for typ in typy:
			WINDOW.blit(typ, (winPos[0], winPos[1]))
			winPos[0] += ROZMIAR_POLA
		pygame.display.update()

		wybrano = False
		while not wybrano:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					ktory = math.floor(pygame.mouse.get_pos()[0] / ROZMIAR_POLA)
					wybrano = True
		return typyChar[ktory]

	def getRozmiar(self):
		return self.__rozmiar

	def getOrganizm(self, x, y):
		return self.__organizmy[x][y]

	@property
	def rozmiar(self):
		return self.__rozmiar

	@property
	def zajetePola(self):
		return self.__zajetePola

	def zajmijPole(self, x, y):
		self.__zajetePola[x][y] = 2

	@property
	def organizmy(self):
		return self.__organizmy