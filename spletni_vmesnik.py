import bottle
from bottle import get, post, run, template, request, redirect
import modeli
import hashlib
@get('/')
def glavna_stran():
    poizvedba = modeli.mozne_valute()
    kriptovalute = [
        (kriptovaluta[1],kriptovaluta[0],kriptovaluta[2],'/trg-kriptovalut/{}/'.format(kriptovaluta[0]))
        for kriptovaluta in poizvedba
    ]
    return template(
        'glavna_stran',
        kriptovalute = kriptovalute)
   

@get('/trg-kriptovalut/')
@get('/trg-kriptovalut/<kratica>/')
def podatki_o_kriptovaluti(kratica = 'BTC'):
    return kratica


SKRIVNOST = 'moja skrivnost'


def prijavljen_uporabnik():
    return request.get_cookie('prijavljen', secret=SKRIVNOST) == 'da'


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
run(reloader = True)
