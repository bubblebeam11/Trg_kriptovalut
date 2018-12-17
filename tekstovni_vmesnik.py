import modeli
import sqlite3
import matplotlib
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
    izbira = int(input(("Izpisi mozne kriptovalute: ")))
    if izbira == 0:
        for kripto in mozne_valute():
            print(kripto)

def trenutek_tecaj(kripto):
    poizvedba = """ 
        SELECT trenutek,
        tecaj
        FROM tecaj
        WHERE kriptovaluta == "BTC"
        """.format(kripto)
    print(conn.execute(poizvedba).fetchall())
def risi_graf(kratica):
    return 0
def main():
    print('Pozdravljeni na trgu kriptovalut!')
    pokazi_moznosti()
trenutek_tecaj("BTC")
#main()
