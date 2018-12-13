import bottle
import modeli
@bottle.get('/')
def glavna_stran():
    return "Dobrodošli v bazi {} filmov in {} oseb!".format(modeli.stevilo_filmov,modeli.stevilo_oseb)

bottle.run(reloader = True)
