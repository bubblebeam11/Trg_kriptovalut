import random
with open('lastnistvo.txt',"r") as datoteka:
    i = 1
    dat2 = open('lastnistvo1.txt',"w")
    for vrstica in datoteka:
        dat2.write(vrstica[:-1] +","+ str(i) +","+ random.choice(["BTC","LTC","NNC","PPC","DOGE"]) + "\n")
        i += 1
    dat2.close()
