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

def ustvari_tabele(conn):
    """
    Ustvari tabele v bazi.
    """
    conn.execute("""
        CREATE TABLE kriptovaluta (
            kratica   TEXT PRIMARY KEY,
            ime       TEXT,
            hitrost   DOUBLE,
            leto_ustanovitve      INTEGER
        );
    """)
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
            do DATE,
            oseba INTEGER NOT NULL REFERENCES oseba(id),
            kriptovaluta TEXT NOT NULL REFERENCES kriptovaluta(kratica)
        );
    """)
    conn.execute("""
        CREATE TABLE trenutek (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cas DATE NOT NULL UNIQUE

        )
    """)
    conn.execute("""
        CREATE TABLE tecaj (
            vrednost  DOUBLE,
            kriptovaluta TEXT NOT NULL REFERENCES kriptovaluta(kratica),
            trenutek INTEGER NOT NULL REFERENCES trenutek(id) 
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

def ustvari_bazo(conn):
    """
    Opravi celoten postopek postavitve baze.
    """
    with conn:
        pobrisi_tabele(conn)
        
        ustvari_tabele(conn)
        uvozi_osebe(conn)
        # uvozi_osebe(conn)
        # uvozi_vloge(conn)
        # uvozi_zanre(conn)

ustvari_bazo(conn)
uvozi_osebe(conn)