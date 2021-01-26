import json
import random


class Pitanja(object):
    __sva_pitanja = []
    pitanja_15 = []

    def __init__(self):
        with open("svaPitanja.json") as sp:
            self.sva_pitanja = json.load(sp)
            sp.close()

    def dohvati_random_pitanja(self):
        indexi = []
        while len(indexi) < 15:
            i = random.randint(0, len(self.sva_pitanja) - 1)
            if i not in indexi:
                indexi.append(i)

        for i in indexi:
            self.pitanja_15.append(self.sva_pitanja[i])

    def __repr__(self):
        return self.__class__.__name__ + "()"


class Pitanje(object):
    jockerov_odgovor = []

    def __init__(self, pitanje, a, b, c, d, tocan):
        self.__pitanje = pitanje
        self.__oznake = ["A", "B", "C", "D"]
        self.__odgovori = [a, b, c, d]
        self.__tocan_odgovor = tocan

    @property
    def pitanje(self):
        return self.__pitanje

    @property
    def oznake(self):
        return self.__oznake

    @oznake.setter
    def oznake(self, oznake):
        self.__oznake = oznake

    @property
    def odgovori(self):
        return self.__odgovori

    @odgovori.setter
    def odgovori(self, odgovori):
        self.__odgovori = odgovori

    @property
    def tocan_odgovor(self):
        return self.__tocan_odgovor

    def je_tocan(self, ponudeni):
        return ponudeni == self.tocan_odgovor

    def izbrisi_odgovor(self):
        preostale_oznake = []
        preostali_odgovori = []
        for o in self.jockerov_odgovor:
            if o == "A":
                preostale_oznake.append(self.oznake[0])
                preostali_odgovori.append(self.odgovori[0])
            elif o == "B":
                preostale_oznake.append(self.oznake[1])
                preostali_odgovori.append(self.odgovori[1])
            elif o == "C":
                preostale_oznake.append(self.oznake[2])
                preostali_odgovori.append(self.odgovori[2])
            else:
                preostale_oznake.append(self.oznake[3])
                preostali_odgovori.append(self.odgovori[3])
        self.oznake = preostale_oznake
        self.odgovori = preostali_odgovori

    def __repr__(self):
        return self.__class__.__name__ + '(%r, %r, %r, %r, %r, %r)' % \
               (self.pitanje, self.odgovori[0], self.odgovori[1],
                self.odgovori[2], self.odgovori[3], self.tocan_odgovor)

    def __str__(self):
        return self.pitanje + '\nA: ' + self.odgovori[0] + '\nB: ' + self.odgovori[1] + '\nC: ' + \
               self.odgovori[2] + '\nD: ' + self.odgovori[3] + '\ntocan odgovor: ' + self.tocan_odgovor


class Jocker(object):
    __svi_jockeri = ["pitaj_publiku", "zovi", "pola_pola"]
    __jocker = ""

    def __init__(self, jocker=""):
        if jocker in self.svi_jockeri:
            self.__jocker = jocker
            self.svi_jockeri.remove(jocker)

    @property
    def svi_jockeri(self):
        return self.__svi_jockeri

    @property
    def jocker(self):
        return self.__jocker

    @jocker.setter
    def jocker(self, jocker):
        self.__jocker = jocker

    @staticmethod
    def pitaj_publiku(lista_oznaka):
        suma_vjerojatnosti = 100
        rezultat = []
        zamjena = lista_oznaka[:]  # kopirana lista oznaka

        for i in range(len(zamjena) - 1):
            izabrani_odgovor = random.choice(zamjena)
            zamjena.remove(izabrani_odgovor)
            postotak = random.randint(0, suma_vjerojatnosti)
            suma_vjerojatnosti -= postotak
            rezultat.append([izabrani_odgovor, postotak])

        rezultat.append([zamjena[0], suma_vjerojatnosti])  # rezultat = [[oznaka, postotak],...]
        rezultat.sort(key=lambda x: x[0])  # sortira rezultat tako da oznake budu ["A", "B", "C", "D"]

        return rezultat

    @staticmethod
    def zovi(lista_odgovora):
        return random.randint(0, len(lista_odgovora) - 1)

    @staticmethod
    def pola_pola(tocan):
        odgovori = ["A", "B", "C", "D"]
        rezultat = [tocan]
        odgovori.remove(tocan)
        rezultat.append(random.choice(odgovori))
        rezultat.sort()

        return rezultat

    def __str__(self):
        return self.jocker.title()

    def __repr__(self):
        return self.__class__.__name__ + "(%s)" % self.jocker


class Igrac(object):
    __iznosi = [0, 100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]

    def __init__(self, ime):
        self.__ime = ime
        self.__iznos_ukupno = 0
        self.__prijedeni_prag = 0

    @property
    def ime(self):
        return self.__ime

    @property
    def iznos_ukupno(self):
        return self.__iznos_ukupno

    @iznos_ukupno.setter
    def iznos_ukupno(self, iznos):
        self.__iznos_ukupno = iznos

    @property
    def prijedeni_prag(self):
        return self.__prijedeni_prag

    @prijedeni_prag.setter
    def prijedeni_prag(self, prag):
        self.__prijedeni_prag = prag

    @property
    def iznosi(self):
        return self.__iznosi

    def __str__(self):
        return self.ime.title() + ', ukupan iznos: ' + str(self.iznos_ukupno) + \
               ', prijeđeni prag: ' + str(self.prijedeni_prag)

    def __repr__(self):
        return self.__class__.__name__ + '(%r)' % self.__ime


class PrikazIgre(object):
    @staticmethod
    def odvoji_redak():
        print("*" * 50)

    def prikazi_pocetak_igre(self):
        self.odvoji_redak()
        print("*" * 12 + "TKO ŽELI BITI MILIJUNAŠ " + "*" * 13)
        self.odvoji_redak()

    @staticmethod
    def prikazi_unos_imena():
        return input("Unesi ime: ")

    @staticmethod
    def prikazi_pitanje(pitanje_objekt, broj_pitanja, iznos):
        print(str(broj_pitanja) + ". Pitanje (" + str(iznos) + " kn): ")
        print(pitanje_objekt.pitanje)
        for i in range(len(pitanje_objekt.odgovori)):
            if pitanje_objekt.oznake[i] == "A":
                print(">>A: " + pitanje_objekt.odgovori[i])
            elif pitanje_objekt.oznake[i] == "B":
                print(">>B: " + pitanje_objekt.odgovori[i])
            elif pitanje_objekt.oznake[i] == "C":
                print(">>C: " + pitanje_objekt.odgovori[i])
            else:
                print(">>D: " + pitanje_objekt.odgovori[i])

    @staticmethod
    def prikazi_mogucnosti_za_nastavak():
        print("Upišite 1 ako želite odustati.\n"
              "Upišite 2 ako želite koristiti jockera.\n"
              "Upišite 3 ako želite odgovoriti.")
        return input("Vaša odluka: ")

    @staticmethod
    def ispisi_osvojeni_iznos(iznos):
        osvojeni_iznos = " Osvojili ste: " + str(iznos) + " kn "
        duljina = 50 - len(osvojeni_iznos)
        print("*" * (duljina // 2) + osvojeni_iznos + "*" * (duljina - duljina // 2))

    @staticmethod
    def igrac_odgovara():
        return input(">>Vaš konačan odgovor je: ")

    @staticmethod
    def ispis_poruke_o_odgovoru(odgovor, tocan_odgovor=""):
        if odgovor:
            print("Točan odgovor!")
        else:
            print("Pogrešan odgovor!")
            print("Točan odgovor je: " + tocan_odgovor)

    @staticmethod
    def prikazi_prag(prag):
        if prag == 1000:
            print("*" * 9 + " Prešli ste prvi prag (1000 kn) " + "*" * 9)
        else:
            print("*" * 8 + " Prešli ste drugi prag (32000 kn) " + "*" * 8)

    @staticmethod
    def prikazi_odluku_o_nastavku():
        return input("Želite li ponovno igrati (da/ne)? ")

    @staticmethod
    def prikazi_jockere(lista_jockera):
        if not lista_jockera:
            print("Svi jockeri su iskorišteni.")
            return
        else:
            print("Preostali jockeri na izboru: ")
            for i in range(len(lista_jockera)):
                if lista_jockera[i] == "pitaj_publiku":
                    print("{}) >>Pitaj publiku".format(i + 1))
                elif lista_jockera[i] == "zovi":
                    print("{}) >>Zovi!".format(i + 1))
                else:
                    print("{}) >>Pola - pola".format(i + 1))

            return input("Unesite broj jockera kojeg želite koristit: ")

    def prikazi_jockerov_odgovor(self, jocker, pitanje_objekt, broj_pitanja, iznos):
        if jocker == "pitaj_publiku":
            print(str(broj_pitanja) + ". Pitanje (" + str(iznos) + " kn): ")
            print(pitanje_objekt.pitanje)
            for i in range(len(pitanje_objekt.odgovori)):
                if pitanje_objekt.oznake[i] == "A":
                    print(">>A: " + pitanje_objekt.odgovori[i] + " - " +
                          str(pitanje_objekt.jockerov_odgovor[i][1]) + "%")
                elif pitanje_objekt.oznake[i] == "B":
                    print(">>B: " + pitanje_objekt.odgovori[i] + " - " +
                          str(pitanje_objekt.jockerov_odgovor[i][1]) + "%")
                elif pitanje_objekt.oznake[i] == "C":
                    print(">>C: " + pitanje_objekt.odgovori[i] + " - " +
                          str(pitanje_objekt.jockerov_odgovor[i][1]) + "%")
                else:
                    print(">>D: " + pitanje_objekt.odgovori[i] + " - " +
                          str(pitanje_objekt.jockerov_odgovor[i][1]) + "%")
        else:
            self.prikazi_pitanje(pitanje_objekt, broj_pitanja, iznos)
            if jocker == "zovi":
                print(">>>Jocker zovi predlaže odgovor " + pitanje_objekt.oznake[pitanje_objekt.jockerov_odgovor] +
                      ": " + pitanje_objekt.odgovori[pitanje_objekt.jockerov_odgovor])


class Igra(object):
    def __init__(self, prikaz=None):
        self.__prikaz = prikaz
        self.__pitanja = Pitanja()
        self.__broj_pitanja = 1
        self.__jocker = Jocker()
        self.__igrac = None

    @property
    def prikaz(self):
        return self.__prikaz

    @property
    def pitanja(self):
        return self.__pitanja

    @pitanja.setter
    def pitanja(self, pitanja):
        self.__pitanja = pitanja

    @property
    def broj_pitanja(self):
        return self.__broj_pitanja

    @property
    def jocker(self):
        return self.__jocker

    @jocker.setter
    def jocker(self, jocker):
        self.__jocker = jocker

    @property
    def igrac(self):
        return self.__igrac

    @igrac.setter
    def igrac(self, igrac):
        self.__igrac = igrac

    def igranje_milijunasa(self):
        self.prikaz.prikazi_pocetak_igre()
        self.unos_igraca()
        self.odabir_pitanja()
        for p in self.pitanja.pitanja_15:
            trenutno_pitanje = self.postavljanje_pitanja(p)
            odgovor = False
            print("Tocan odgovor je: ", trenutno_pitanje.tocan_odgovor)
            while True:
                odluka = self.odluka_o_nastavku()
                if odluka == "1":
                    # igrac je odustao
                    self.izracun_osvojenog_iznosa()
                    break
                elif odluka == "2":
                    # igrac koristi jockera
                    self.jocker = Jocker(self.koristenje_jockera())
                    self.postavi_jockerov_odgovor(trenutno_pitanje)
                elif odluka == "3":
                    # igrac odgovara
                    odgovor = self.odgovaranje_na_pitanje(trenutno_pitanje)
                    break

            if odluka == "1" or (odluka == "3" and not odgovor):
                break

            self.__broj_pitanja += 1

        if self.__broj_pitanja == 16:
            # igrac je odgovorio na sva pitanja tocno
            self.izracun_osvojenog_iznosa()

        if self.ponovno_pokretanje_igre():
            main()

    def unos_igraca(self):
        while True:
            ime = self.prikaz.prikazi_unos_imena()
            if ime.strip():
                self.prikaz.odvoji_redak()
                self.igrac = Igrac(ime)
                break

    def odabir_pitanja(self):
        self.pitanja = Pitanja()
        self.pitanja.dohvati_random_pitanja()

    def postavljanje_pitanja(self, pitanje_objekt):
        p = Pitanje(pitanje_objekt['question'], pitanje_objekt['A'], pitanje_objekt['B'],
                    pitanje_objekt['C'], pitanje_objekt['D'], pitanje_objekt['answer'])
        self.prikaz.prikazi_pitanje(p, self.broj_pitanja, self.igrac.iznosi[self.broj_pitanja])
        self.prikaz.odvoji_redak()
        return p

    def odluka_o_nastavku(self):
        while True:
            odgovor = self.prikaz.prikazi_mogucnosti_za_nastavak()
            self.prikaz.odvoji_redak()
            if odgovor == "1" or odgovor == "2" or odgovor == "3":
                return odgovor

    def izracun_osvojenog_iznosa(self):
        self.prikaz.ispisi_osvojeni_iznos(self.igrac.iznos_ukupno)
        self.prikaz.odvoji_redak()

    def koristenje_jockera(self):
        while True:
            odluka = self.prikaz.prikazi_jockere(self.jocker.svi_jockeri)
            self.prikaz.odvoji_redak()
            if odluka is None:
                return
            else:
                try:
                    odluka = int(odluka)
                    if 0 < odluka <= len(self.jocker.svi_jockeri):
                        return self.jocker.svi_jockeri[odluka - 1]
                except ValueError:
                    pass

    def postavi_jockerov_odgovor(self, pitanje_objekt):
        if self.jocker.jocker == "pitaj_publiku":
            pitanje_objekt.jockerov_odgovor = self.jocker.pitaj_publiku(pitanje_objekt.oznake)
        elif self.jocker.jocker == "zovi":
            pitanje_objekt.jockerov_odgovor = self.jocker.zovi(pitanje_objekt.odgovori)
        elif self.jocker.jocker == "pola_pola":
            pitanje_objekt.jockerov_odgovor = self.jocker.pola_pola(pitanje_objekt.tocan_odgovor)
            pitanje_objekt.izbrisi_odgovor()
        self.prikaz.prikazi_jockerov_odgovor(self.jocker.jocker, pitanje_objekt,
                                             self.broj_pitanja, self.igrac.iznosi[self.broj_pitanja])
        self.prikaz.odvoji_redak()

    def odgovaranje_na_pitanje(self, pitanje_objekt):
        while True:
            odgovor = self.prikaz.igrac_odgovara()
            if odgovor.upper() in pitanje_objekt.oznake:
                tocan = pitanje_objekt.je_tocan(odgovor.upper())
                if tocan:
                    # igrac je tocno odgovorio
                    self.prikaz.odvoji_redak()
                    self.prikaz.ispis_poruke_o_odgovoru(True)
                    self.prikaz.odvoji_redak()
                    self.igrac.iznos_ukupno = self.igrac.iznosi[self.broj_pitanja]
                    if self.igrac.iznos_ukupno == 1000 or self.igrac.iznos_ukupno == 32000:
                        self.igrac.prijedeni_prag = self.igrac.iznos_ukupno
                        self.prikaz.prikazi_prag(self.igrac.prijedeni_prag)
                        self.prikaz.odvoji_redak()
                    return True
                else:
                    # igrac je krivo odgovorio
                    self.prikaz.odvoji_redak()
                    self.prikaz.ispis_poruke_o_odgovoru(False, pitanje_objekt.tocan_odgovor)
                    self.prikaz.odvoji_redak()
                    self.prikaz.ispisi_osvojeni_iznos(self.igrac.prijedeni_prag)
                    self.prikaz.odvoji_redak()
                    return False

    def ponovno_pokretanje_igre(self):
        while True:
            odluka = self.prikaz.prikazi_odluku_o_nastavku()
            if odluka.upper() == "NE":
                return False
            elif odluka.upper() == "DA":
                return True


def main():
    prikaz = PrikazIgre()
    igra = Igra(prikaz)
    igra.igranje_milijunasa()


if __name__ == "__main__":
    main()
