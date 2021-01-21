import json
import random


class Pitanja(object):
    __svaPitanja = []
    pitanja15 = []

    def __init__(self):
        with open('svaPitanja.json') as sp:
            self.svaPitanja = json.load(sp)
            sp.close()

    
    def DohvatiRandomPitanja(self):
        indexi = []
        while len(indexi) < 15:
            i = random.randint(0, len(self.svaPitanja) - 1)
            if i not in indexi:
                indexi.append(i)

        for i in indexi:
            self.pitanja15.append(self.svaPitanja[i])
    
    def __repr__(self):
        return self.__class__.__name__ + '()'


class Pitanje(object):
    def __init__(self, pitanje, a, b, c, d, tocan):
        self.__pitanje = pitanje
        self.__odgovorA = a
        self.__odgovorB = b
        self.__odgovorC = c
        self.__odgovorD = d
        self.__tocanOdgovor = tocan

    @property
    def pitanje(self):
        return self.__pitanje
    
    @property
    def odgovorA(self):
        return self.__odgovorA
    
    @property
    def odgovorB(self):
        return self.__odgovorB
    
    @property
    def odgovorC(self):
        return self.__odgovorC
    
    @property
    def odgovorD(self):
        return self.__odgovorD
    
    @property
    def tocanOdgovor(self):
        return self.__tocanOdgovor

    def JeTocan(self, ponudeni):
        if ponudeni == self.tocanOdgovor:
            return True
        else:
            return False

    def __repr__(self):
        return self.__class__.__name__ + '(%r, %r, %r, %r, %r, %r)' % (self.__pitanje, self.__odgovorA, self.__odgovorB, self.__odgovorC, self.__odgovorD, self.__tocanOdgovor)

    def __str__(self):
        return self.__pitanje + '\nA: ' + self.__odgovorA + '\nB: ' + self.__odgovorB + '\nC: ' + self.__odgovorC + '\nD: ' + self.__odgovorD + '\ntocan odgovor: ' + self.__tocanOdgovor


class Jocker (object):
    __sviJockeri = ['pitajPubliku', 'zovi', 'polaPola']
    __jocker = ""

    def __init__(self, jocker = ""):
        if jocker in self.sviJockeri:
            self.__jocer = jocker
            self.sviJockeri.remove(jocker)

    @property
    def sviJockeri(self):
        return self.__sviJockeri

    @property
    def jocker(self):
        return self.__jocker
    @jocker.setter
    def jocker(self, jocker):
        self.__jocker = jocker

    @staticmethod
    def PitajPubliku():
        odgovori = ['A', 'B', 'C', 'D']
        sumaVjerojatnosti = 100
        rezultat = []

        for i in range(3):
            izabraniOdgovor = random.choice(odgovori)
            odgovori.remove(izabraniOdgovor)
            postotak = random.randint(0, sumaVjerojatnosti)
            sumaVjerojatnosti -= postotak
            rezultat.append(izabraniOdgovor)
            rezultat.append(postotak)

        rezultat.append(odgovori[0])
        rezultat.append(sumaVjerojatnosti)

        return rezultat

    @staticmethod
    def Zovi():
        return random.choice(['A', 'B', 'C', 'D'])

    @staticmethod
    def PolaPola(tocan):
        odgovori = ['A', 'B', 'C', 'D']
        rezultat = [tocan]
        odgovori.remove(tocan)
        rezultat.append(random.choice(odgovori))
        rezultat.sort()

        return rezultat

    def __str__(self):
        return self.__jocker.title()
    
    def __repr__(self):
        return self.__class__.__name__ + '(%s)' % (self.__jocker)


class Igrac(object):
    def __init__(self, ime):
        self.__ime = ime
        self.__iznosUkupno = 0
        self.__prijedeniPrag = 0

    @property
    def ime(self):
        return self.__ime

    @property
    def iznosUkupno(self):
        return self.__iznosUkupno
    @iznosUkupno.setter
    def iznosUkupno(self, iznos):
        self.__iznosUkupno = iznos

    @property
    def prijedeniPrag(self):
        return self.__prijedeniPrag
    @prijedeniPrag.setter
    def prijedeniPrag(self, prag):
        self.__prijedeniPrag = prag

    def __str__(self):
        return self.__ime.title() + ', ukupan iznos: ' + str(self.__iznosUkupno) + ', prijeđeni prag: ' + str(self.__prijedeniPrag)
    
    def __repr__(self):
        return self.__class__.__name__ + '(%r)' % (self.__ime)


class PrikazIgre():

    def PrikaziPocetakIgre(self):
        print("*" * 50)
        print("*" * 12 + " TKO ŽELI BITI MILIJUNAŠ " + "*" * 13)
        print("*" * 50)

    def UnesiIgraca(self):
        while True:
            ime = input("Unesi ime: ")
            if ime.strip():
                print("*" * 50)
                return ime.strip()

    def PrikaziPitanje(self, pitanjeObjekt, redniBroj):
        oznakaOdgovora = ['A', 'B', 'C', 'D']
        odgovori = [pitanjeObjekt.odgovorA, pitanjeObjekt.odgovorB, pitanjeObjekt.odgovorC, pitanjeObjekt.odgovorD]
        print(str(redniBroj) + ". Pitanje: ")
        print(pitanjeObjekt.pitanje)
        for i in range(4):
            print(">>" + oznakaOdgovora[i] + ": " + odgovori[i])
        print("*" * 50)

    def PrikaziPrag(self, iznosPraga):
        if iznosPraga == 1000:
            print("*" * 9 + " Prešli ste prvi prag (1000 kn) " + "*" * 9)
        else:
            print("*" * 8 + " Prešli ste drugi prag (32000 kn) " + "*" * 8)
        print("*" * 50)

    def PrikaziOdlukuZaNastavak(self):
        print()
        while True:
            print("Upišite 1 ako želite odustati.\nUpišite 2 ako želite koristiti jockera.\nUpišite 3 ako želite odgovoriti.")
            odg = input("Vaša odluka: ")
            if odg == "1" or odg == "2" or odg == "3":
                return odg

    def PonudiMoguceJockere(self, listaJockera):
        print("Preostali jockeri na izboru: ")
        for i in range(len(listaJockera)):
            if listaJockera[i] == "pitajPubliku":
                print("{}) >>Pitaj publiku".format(i+1))
            elif listaJockera[i] == "zovi":
                print("{}) >>Zovi!".format(i+1))
            else:
                print("{}) >>Pola - pola".format(i+1))

        while True:
            odluka = input("Unesite broj jockera kojeg želite koristit: ")
            try:
                odluka = int(odluka)
                if odluka > 0 and odluka <= len(listaJockera):
                    return listaJockera[odluka-1]
                else:
                    pass
            except ValueError:
                pass


    def PrikaziJockerOdgovor(self, jocker, pitanje_objekt):
        print()
        if jocker == "pitajPubliku":
            oznakaOdgovora = jocker.PitajPubliku()
            odgovori = [pitanje_objekt.odgovorA, pitanje_objekt.odgovorB, pitanje_objekt.odgovorC, pitanje_objekt.odgovorD]
            print(pitanje_objekt.pitanje)
            for oznaka in oznakaOdgovora:
                if oznaka == "A":
                    print(">>A: " + odgovori[0])
                elif oznaka == "B":
                    print(">>B: " + odgovori[1])
                elif oznaka == "C":
                    print(">>C: " + odgovori[2])
                else:
                    print(">>D: " + odgovori[3])
            print("*" * 50)
        elif jocker == "zovi":
            pass
        else:
            pass
        
    def PrikaziJockerOdgovorPolaPola(self, jocker, pitanje_objekt):
        pass
        
    def PrikaziJockerOdgovorPitajPubliku(self,jocker):
        pass

    def PrikaziJockerOdgovorZovi(self,jocker):
        pass

    def korisnikOdgovara(self, pitanje_objekt):
        while True:
            odabir = input(">>Vaš konačan odgovor je: ")
            if odabir.upper() == "A" or odabir.upper() == "B" or odabir.upper() == "C" or odabir.upper() == "D":
                if odabir.upper() == pitanje_objekt.tocanOdgovor:
                    print("Točan odgovor!")
                    return True
                else:
                    print("Pogrešan odgovor!")
                    return False


def main():
    pi = PrikazIgre()
    pi.PrikaziPocetakIgre()
    pi.UnesiIgraca()

    svaPitanja = Pitanja()
    svaPitanja.DohvatiRandomPitanja()
    j = Jocker()

    i = 1
    for p in svaPitanja.pitanja15:
        trenutnoPitanje = Pitanje(p['question'], p['A'], p['B'], p['C'], p['D'], p['answer'])
        pi.PrikaziPitanje(trenutnoPitanje, i)
        
        odluka = ""
        
        while odluka != "3":
            odluka = pi.PrikaziOdlukuZaNastavak()
            if odluka == "1":
                # igrac je odustao
                pass
            elif odluka == "2":
                # igrac koristi jockera
                j = pi.PonudiMoguceJockere(j.sviJockeri)
                print("Izabrani Jocker: " + j)
                

        # igrac odgovara
        odgovor = pi.korisnikOdgovara(trenutnoPitanje)
        if odgovor == False:
            # igrac je krivo odgovorio
            break
        
        
        i += 1
        if i == 2:
            break


if __name__ == "__main__":
    main()






