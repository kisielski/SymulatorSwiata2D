from Ruchy import Ruchy
from Swiat import Swiat
from Trawa import Trawa
from Mlecz import Mlecz
from Guarana import Guarana
from WilczeJagody import WilczeJagody
from BarszczSosnowskiego import BarszczSosnowskiego
from Owca import Owca
from Wilk import Wilk
from Antylopa import Antylopa
from Lis import Lis
from Zolw import Zolw
from Cyberowca import Cyberowca

class IO:

	def __init__(self):
		pass

	def zapis(self, swiat, sciezka, com):
		f = open(sciezka, "w")
		for i in range(swiat.rozmiar):
				for j in range(swiat.rozmiar):
					if swiat.zajetePola[i][j] != 0:
						org = swiat.organizmy[i][j]
						f.write(f"{org.typ};{org.x};{org.y}\n")
		f.close()
		com.wyczysc()
		info = f"Zapisano do {sciezka}"
		com.dodaj(info)

	def odczyt(self, swiat, sciezka, com, czlowiek):
		f = open(sciezka, "r")
		for i in range(swiat.rozmiar):
				for j in range(swiat.rozmiar):
					swiat.wyczyscPole(i, j)
		for line in f:
			licznik = 0
			for dane in line.split(";"):
				if licznik == 0:
					typ = dane
				elif licznik == 1:
					x = int(dane)
				elif licznik == 2:
					y = int(dane)
				licznik += 1
			if typ != '*':
				self.resp(swiat, x, y, typ)
			else:
				czlowiek.przesun(x, y)
		f.close()
		com.wyczysc()
		info = f"Odczytano z {sciezka}"
		com.dodaj(info)

	@staticmethod
	def resp(swiat, x, y, typ):
		if typ == 'T':
			Trawa(x, y, swiat)
		elif typ == 'M':
			Mlecz(x, y, swiat)
		elif typ == 'G':
			Guarana(x, y, swiat)
		elif typ == 'J':
			WilczeJagody(x, y, swiat)
		elif typ == 'B':
			BarszczSosnowskiego(x, y, swiat)
		elif typ == 'O':
			Owca(x, y, swiat)
		elif typ == 'W':
			Wilk(x, y, swiat)
		elif typ == 'A':
			Antylopa(x, y, swiat)
		elif typ == 'L':
			Lis(x, y, swiat)
		elif typ == 'Z':
			Zolw(x, y, swiat)
		elif typ == 'C':
			Cyberowca(x, y, swiat)