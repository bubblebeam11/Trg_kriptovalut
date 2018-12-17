import sqlite3

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


def mozne_valute():
    """
    Funkcija, ki vrne vse možne valute.
    """
    poizvedba = """
        SELECT *
        FROM kriptovaluta
    """
    print(conn.execute(poizvedba).fetchall())
    return conn.execute(poizvedba).fetchall()
#mozne_valute()