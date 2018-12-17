import csv
from modeli import conn

def pobrisi_tabele(conn):
    """
    Pobriše tabele iz baze.
    """
    conn.execute("DROP TABLE IF EXISTS lastnistvo;")
    conn.execute("DROP TABLE IF EXISTS tecaj;")
    conn.execute("DROP TABLE IF EXISTS trenutek;") 
    conn.execute("DROP TABLE IF EXISTS oseba;")
    conn.execute("DROP TABLE IF EXISTS kriptovaluta;")

def ustvari_tabele(conn):
    """
    Ustvari tabele v bazi.
    """
    print("Ustvarjam tabele...")
    conn.execute("""
        CREATE TABLE kriptovaluta (
            kratica   TEXT PRIMARY KEY,
            ime       TEXT,
            leto_ustanovitve      INTEGER
        );
    """)
    conn.execute("""
        CREATE TABLE oseba (
            id  INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT
        );
    """)
    conn.execute("""
        CREATE TABLE lastnistvo (
            id  INTEGER PRIMARY KEY ,
            kolicina DOUBLE,
            od DATE,
            do DATE,
            oseba INTEGER REFERENCES oseba(id),
            kriptovaluta TEXT REFERENCES kriptovaluta(kratica)
            
        );
    """)

    conn.execute("""
        CREATE TABLE trenutek (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cas DATE 
        )
    """)

    conn.execute("""
        CREATE TABLE tecaj (
            kriptovaluta TEXT NOT NULL REFERENCES kriptovaluta(kratica),
            trenutek INTEGER NOT NULL REFERENCES trenutek(id), 
            tecaj DECIMAL,
            PRIMARY KEY(kriptovaluta, trenutek) 
        )
    """)
def uvozi_osebe(conn):
    """
    Uvozi podatke o osebah.
    """
    conn.execute("DELETE FROM oseba;")
    with open('podatki/username.csv') as datoteka:
        podatki = csv.reader(datoteka)
        next(podatki)
        poizvedba = """
            INSERT INTO oseba VALUES (?,?)
        """
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)


def uvozi_lastnistvo(conn):
    """
    Uvozi podatke o lastnistvu.
    """
    conn.execute("DELETE FROM lastnistvo;")
    with open('podatki/lastnistvo.csv') as datoteka:
        podatki = csv.reader(datoteka)
        poizvedba = """
            INSERT INTO lastnistvo VALUES (?,?,?,?,?,?)
        """
        for vrstica in podatki:
            print(vrstica)
            conn.execute(poizvedba, vrstica)
def uvozi_tecaj(conn):
    """
    Uvozi podatke o tecajih.
    """
    conn.execute("DELETE FROM tecaj;")
    with open('podatki/tecaj.csv') as datoteka:
        podatki = csv.reader(datoteka)
        i = 1
        trenutek_poizvedba = """ SELECT id FROM trenutek WHERE cas = ? """

        poizvedba = """
            INSERT INTO tecaj VALUES ( ?, ?, ? )
        """
        for vrstica in podatki:
            vrstica[1], = conn.execute(trenutek_poizvedba,[vrstica[1]]).fetchone()
            conn.execute(poizvedba, vrstica)

def uvozi_kriptovaluta(conn):
    """
    Uvozi podatke o kriptovalutah
    """
    conn.execute("DELETE FROM kriptovaluta;")
    with open('podatki/kriptovaluta.csv') as datoteka:
        podatki = csv.reader(datoteka)
        
        poizvedba = """
            INSERT INTO kriptovaluta VALUES (?,?,?)
        """
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_trenutek(conn):
    """
    Uvozi podatke o trenutkih
    """
    conn.execute("DELETE FROM trenutek;")
    with open('podatki/trenutek.csv') as datoteka:
        podatki = csv.reader(datoteka)
        
        i = 1
        poizvedba = """
            INSERT INTO trenutek VALUES (?,?)
        """
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)
            


def ustvari_bazo(conn):
    """
    Opravi celoten postopek postavitve baze.
    """
    with conn:
        ustvari_tabele(conn)
        uvozi_osebe(conn)
        uvozi_kriptovaluta(conn)
        uvozi_trenutek(conn)
        uvozi_tecaj(conn)
        uvozi_lastnistvo(conn)
pobrisi_tabele(conn)
ustvari_bazo(conn)