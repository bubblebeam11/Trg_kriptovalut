from modeli import*
import sqlite3
import matplotlib.pyplot as plt
conn = sqlite3.connect('kriptovalute.db')
conn.execute('PRAGMA foreign_keys = ON')


def pokazi_moznosti():
    print('Moznosti:')
    izbira = int(input(("""1 = Izpisi mozne kriptovalute\n2 = Narisi graf\n3 = Izpisi lastnistva\n""")))
    if izbira == 1:
        valute = mozne_valute()
        i = 1
        for kripto in valute:
            print("{}) {}({}) , leto ustanovitve: {}".format(i,kripto[1],kripto[0],kripto[2]))
            i +=1
        pokazi_moznosti()
    if izbira == 2:
        izbranaValuta = input(("Izberi Kriptovaluto: "))
        risi_graf(izbranaValuta)
        pokazi_moznosti()
    if izbira == 3:
        uporabnik = input("Vnesi uporabniško ime: ")
        lastnistva = lastnistva_uporabnika(uporabnik)
        print("Uporabnik {} ima opravljene naslednje nakupe:\n".format(uporabnik))
        i = 1
        for lastnistvo in lastnistva:
            print("{}) {} {} od {} do {}".format(i,lastnistvo[1],lastnistvo[0],lastnistvo[2],lastnistvo[3]))
            i += 1
def main():
    print('Pozdravljeni na trgu kriptovalut!')
    pokazi_moznosti()



main()
