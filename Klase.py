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
        while (len(indexi) < 15):
            i = random.randint(0, len(self.svaPitanja)-1)
            if(i not in indexi):
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
        if(ponudeni == self.tocanOdgovor):
            return True
        else:
            return False

    def __repr__(self):
        return self.__class__.__name__ + '(%r, %r, %r, %r, %r, %r)' % (self.__pitanje, self.__odgovorA, self.__odgovorB, self.__odgovorC, self.__odgovorD, self.__tocanOdgovor)

    def __str__(self):
        return self.__pitanje + '\nA: ' + self.__odgovorA + '\nB: ' + self.__odgovorB + '\nC: ' + self.__odgovorC + '\nD: ' + self.__odgovorD + '\ntocan odgovor: ' + self.__tocanOdgovor


class Jocker (object):
    sviJockeri = ['pitajPubliku', 'zovi', 'polaPola']

    def __init__(self, jocker):
        if(jocker in self.sviJockeri):
            self.__jocer = jocker
            self.sviJockeri.remove(jocker)
        else:
            print('Jocker je vec iskoristen')

    @property
    def jocker(self):
        return self.__jocker

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


##2. tjedan
class PrikazIgre():

    def PrikaziPocetakIgre(self):
        print("*" * 50)
        print("*" * 12 + " TKO ŽELI BITI MILIJUNAŠ " + "*" * 13)
        print("*" * 50)

    def UnesiIgraca(self):
        while(True):
            ime = input("Unesi ime: ")
            if(ime.strip()):
                print("*"*50)
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
        if(iznosPraga == 1000):
            print("*" * 9 + " Prešli ste prvi prag (1000 kn) " + "*" * 9)
        else:
            print("*" * 8 + " Prešli ste drugi prag (32000 kn) " + "*" * 8)
        print("*" * 50)

    def PrikaziOdlukuZaNastavak(self):
        print()
        while(True):
            print("Upišite 1 ako želite odustati.\nUpišite 2 ako želite koristiti jockera.\nUpišite 3 ako želite odgovoriti.")
            odg = input("Vaša odluka: ")
            if(odg == "1" or odg == "2" or odg == "3"):
                return odg

'''
    def PrikaziUpitZaIzlaz(self):
        print()
        while True:
            odg = input("Želite li odustati? (da/ne) ")
            if odg.strip().upper()=="DA":
                return True
            elif odg.strip().upper()=="NE":
                return False

    def PrikaziUpitZaJockera(self):
        print()
        while True:
            odg = input("Želite li koristit jockera? (da/ne) ")
            if odg.strip().upper()=="DA":
                return True
            elif odg.strip().upper()=="NE":
                return False
    
    def PonudiMoguceJockere(self, jocker):
        print("Preostali jockeri na izboru: ")
        for i,j in enumerate(jocker.sviJockeri): 
            if j=="pitajPubliku":
                print("{}) >>Pitaj publiku".format(i+1))
            elif j=="zovi":
                print("{}) >>Zovi!".format(i+1))
            elif j=="polaPola":
                print("{}) >>Pola - pola".format(i+1))

    def korisnikOdgovara(self,ima_jockera,pitanje_objekt):
        #ovdje treba provjeriti hoce li izabrati jockera, odgovoriti na pitanje ili odustati
        #ovisno sto ova metoda vrati  u controlu prosljedivati za primjerene situacije
        while True:
            if ima_jockera:
                print("Za odabir jockera unesi pripadajući broj")
            print("Za odgovor na pitanje unesi A, B, C ili D, a za IZLAZ unesi x")
            print("*"*50)
            odabir=input(">>Unos: ")
            if odabir.lower() == pitanje_objekt.tocanOdgovor:
                #korisnik je tocno odgovorio
                return "tocan"
            elif odabir.lower() == "x":
                #igrac zeli izaci  ->izracunati skupljene novce
                return "izlaz"
            elif odabir.lower() == "1" and int(odabir) <= len(Jocker.sviJockeri):
                odabir=Jocker.sviJockeri[int(odabir)-1]
                jocker=Jocker(odabir) #ovdje se u initi od jockera automatski brise iz mogucih i postavlja se vrijednost(ime) na jocker varijablu u objektu
                print("odabrani dzoker 1",jocker.jocker)
                return jocker
            elif odabir.lower() == "2" and int(odabir) <= len(Jocker.sviJockeri):
                odabir=Jocker.sviJockeri[int(odabir)-1]
                jocker=Jocker(odabir)
                print("odabrani dzoker 2",jocker.jocker)
                return jocker
            elif odabir.lower() == "3" and int(odabir) <= len(Jocker.sviJockeri):
                odabir=Jocker.sviJockeri[int(odabir)-1]
                jocker=Jocker(odabir)
                print("odabrani dzoker 3",jocker.jocker)
                return jocker
            elif odabir.lower() !=pitanje_objekt.tocanOdgovor:
                #krivi odgovor   ->izracunati skupljene novce
                print("Pogrešan odgovor!")
                return "pogresan"
            
    def prikaziJockerOdgovorPolaPola(self,jocker,pitanje_objekt):
        pass
        
    def prikaziJockerOdgovorPitajPubliku(self,jocker):
        pass

    def prikaziJockerOdgovorZovi(self,jocker):
        pass
'''


pi = PrikazIgre()
pi.PrikaziPocetakIgre()
pi.UnesiIgraca()

svaPitanja = Pitanja()
svaPitanja.DohvatiRandomPitanja()

i = 1
for p in svaPitanja.pitanja15:
    trenutnoPitanje = Pitanje(p['question'], p['A'], p['B'], p['C'], p['D'], p['answer'])
    pi.PrikaziPitanje(trenutnoPitanje, i)
    pi.PrikaziOdlukuZaNastavak()
    
    i += 1
