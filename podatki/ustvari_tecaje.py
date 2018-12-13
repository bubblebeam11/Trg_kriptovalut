from math import sin,cos,log10
import random
tecaj = open('tecaj.txt',"w")
trenutek = open('trenutek3.txt')
kratice = ["BTC"]

for kratica in kratice:
    i = 0
    print(kratica)
    for vrstica in trenutek:
            i += 1
            tecaj_v_trenutku = random.uniform(0.1,100) + (1/40)*ord(kratica[0])*abs(100*sin(int(vrstica[8:])*i)*log10(1+abs(i*int(vrstica[-2]))))
            tecaj.write(kratica +","+ vrstica[0:-1] + ","+ str(tecaj_v_trenutku)+"\n")
        
            
tecaj.close()
