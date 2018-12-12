import bottle

@bottle.get('/')
def glavna_stran():
    return "Dobrodošli v bazi {} filmov in {} oseb!".format(100,10)

bottle.run(reloader = True)
