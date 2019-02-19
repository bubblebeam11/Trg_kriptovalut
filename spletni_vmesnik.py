import bottle
import modeli
@bottle.get('/')
def glavna_stran():
    poizvedba = modeli.mozne_valute()
    kriptovalute = [
        (kriptovaluta[1],kriptovaluta[0],kriptovaluta[2])
        for kriptovaluta in poizvedba
    ]
    return bottle.template(
        'glavna_stran',
        kriptovalute = kriptovalute)
   

bottle.run(reloader = True)
