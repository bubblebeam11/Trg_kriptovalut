import csv
from modeli import conn

def pobrisi_tabele(conn):
    """
    Pobriše tabele iz baze.
    """
    conn.execute("DROP TABLE IF EXISTS kriptovaluta;")
    conn.execute("DROP TABLE IF EXISTS lastnistvo;")
    conn.execute("DROP TABLE IF EXISTS oseba;")
    conn.execute("DROP TABLE IF EXISTS vrednost;")
    conn.execute("DROP TABLE IF EXISTS trenutek;")
    conn.execute("DROP TABLE IF EXISTS tecaj;")

def ustvari_tabele(conn):
    """
    Ustvari tabele v bazi.
    """
    conn.execute("""
        CREATE TABLE kriptovaluta (
            kratica   TEXT PRIMARY KEY,
            ime       TEXT,
            
            leto_ustanovitve      INTEGER
        );
    """)
    #hitrost   DOUBLE,
    conn.execute("""
        CREATE TABLE oseba (
            id  INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            dobicek DOUBLE
        );
    """)
    conn.execute("""
        CREATE TABLE lastnistvo (
            id  INTEGER PRIMARY KEY AUTOINCREMENT,
            kolicina DOUBLE,
            od DATE,
            do DATE
        );
    """)
            #oseba INTEGER NOT NULL REFERENCES oseba(id),
            #kriptovaluta TEXT NOT NULL REFERENCES kriptovaluta(kratica)
    conn.execute("""
        CREATE TABLE trenutek (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cas DATE UNIQUE

        )
    """)
    conn.execute("""
        CREATE TABLE tecaj (
            kratica TEXT NOT NULL REFERENCES kriptovaluta(kratica),
            trenutek INTEGER UNIQUE NOT NULL REFERENCES trenutek(cas), 
            vrednost  DOUBLE
            
        );
    """)
def uvozi_osebe(conn):
    """
    Uvozi podatke o osebah.
    """
    conn.execute("DELETE FROM oseba;")
    with open('podatki/username.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO oseba VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_lastnistvo(conn):
    """
    Uvozi podatke o lastnistvu.
    """
    conn.execute("DELETE FROM lastnistvo;")
    with open('podatki/lastnistvo.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO lastnistvo VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_kriptovaluta(conn):
    """
    Uvozi podatke o osebah.
    """
    conn.execute("DELETE FROM kriptovaluta;")
    with open('podatki/kriptovaluta.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO kriptovaluta VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_trenutek(conn):
    """
    Uvozi podatke o osebah.
    """
    conn.execute("DELETE FROM trenutek;")
    with open('podatki/trenutek.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        i = 1
        poizvedba = """
            INSERT INTO trenutek VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)
            
def uvozi_tecaj(conn):
    """
    Uvozi podatke o osebah.
    """
    conn.execute("DELETE FROM tecaj;")
    with open('podatki/tecaj.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        i = 1
        poizvedba = """
            INSERT INTO tecaj VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def ustvari_bazo(conn):
    """
    Opravi celoten postopek postavitve baze.
    """
    with conn:
        ustvari_tabele(conn)
        uvozi_osebe(conn)
        uvozi_lastnistvo(conn)
        uvozi_kriptovaluta(conn)
        uvozi_trenutek(conn)
        uvozi_tecaj(conn)
pobrisi_tabele(conn)
ustvari_bazo(conn)