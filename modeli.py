import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('kriptovalute.db')
conn.execute("PRAGMA foreign_keys = ON")

def commit(fun):
    """
    Dekorator, ki ustvari kurzor, ga poda dekorirani funkciji,
    in nato zapiše spremembe v bazo.
    Originalna funkcija je na voljo pod atributom nocommit.
    """
    def funkcija(*largs, **kwargs):
        ret = fun(conn.cursor(), *largs, **kwargs)
        conn.commit()
        return ret
    funkcija.__doc__ = fun.__doc__
    funkcija.__name__ = fun.__name__
    funkcija.__qualname__ = fun.__qualname__
    fun.__qualname__ += '.nocommit'
    funkcija.nocommit = fun
    return funkcija

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
    XY = trenutek_tecaj(kratica)
    plt.plot(XY[0], XY[1])
    plt.axis([0, 1000, 0, 1000])
    plt.show()

def mozne_valute():
    """
    Funkcija, ki vrne vse možne valute.
    [('LTC', 'Litecoin', 2011), ('NMC', 'Namecoin', 2011), ... ]
    """
    poizvedba = """
        SELECT * from kriptovaluta
    """
    return conn.execute(poizvedba).fetchall()
@post('/prijava/')
def prijava():
    uporabnisko_ime = request.forms.uporabnisko_ime
    geslo = request.forms.geslo
    if modeli.preveri_geslo(uporabnisko_ime, geslo):
        bottle.response.set_cookie(
            'prijavljen', 'da', secret=SKRIVNOST, path='/')
        redirect('/')
    else:
        raise bottle.HTTPError(403, "BOOM!")