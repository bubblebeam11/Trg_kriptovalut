import modeli
import sqlite3
import matplotlib.pyplot as plt
conn = sqlite3.connect('kriptovalute.db')
conn.execute('PRAGMA foreign_keys = ON')

def mozne_valute():
    """
    Funkcija, ki vrne vse možne valute.
    [('LTC', 'Litecoin', 2011), ('NMC', 'Namecoin', 2011), ... ]
    """
    poizvedba = """
        SELECT * from kriptovaluta
    """
    return conn.execute(poizvedba).fetchall()
def pokazi_moznosti():
    print('Moznosti:')
    izbira = int(input(("""1 = Izpisi mozne kriptovalute\n2 = Narisi graf\n3 = Izpisi lastnistva\n""")))
    if izbira == 1:
        
        valute = mozne_valute()
        i = 1
        for kripto in valute:
            print("{}) {}({}) , leto ustanovitve: {}".format(i,kripto[1],kripto[0],kripto[2]))
            i +=1

    if izbira == 2:
        izbranaValuta = input(("Izberi Kriptovaluto: "))
        XY = trenutek_tecaj(izbranaValuta)
        plt.plot(XY[0], XY[1])
        plt.axis([0, 1000, 0, 1000])
        plt.show()
        pokazi_moznosti()
    if izbira == 3:
        uporabnik = input("Vnesi uporabniško ime: ")
        lastnistva = lastnistva_uporabnika(uporabnik)
        print("Uporabnik {} ima opravljene naslednje nakupe:\n".format(uporabnik))
        i = 1
        for lastnistvo in lastnistva:
            print("{}) {} {} od {} do {}".format(i,lastnistvo[1],lastnistvo[0],lastnistvo[2],lastnistvo[3]))
            i += 1

def trenutek_tecaj(kripto):
    poizvedba = """ 
        SELECT trenutek,
        tecaj
        FROM tecaj
        WHERE kriptovaluta = ?
    """
    cur = conn.cursor()
    cur.execute(poizvedba, [kripto])
    podatki = cur.fetchall()
    X = []
    Y = []
    for x,y in podatki:
        X.append(x)
        Y.append(y)
    return (X,Y)

def lastnistva_uporabnika(uporabnik):
    poizvedba = """ 
        SELECT kriptovaluta,
            kolicina,
            od,
            do
        FROM lastnistvo JOIN oseba ON
        (oseba.id = lastnistvo.oseba) 
        WHERE username = ?;
    """
    cur = conn.cursor()
    cur.execute(poizvedba, [uporabnik])
    podatki = cur.fetchall()
    return podatki

def risi_graf(kratica):
    return 0
def main():
    print('Pozdravljeni na trgu kriptovalut!')
    pokazi_moznosti()
main()
