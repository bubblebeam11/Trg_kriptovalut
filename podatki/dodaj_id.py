with open('trenutek.txt',"r") as datoteka:
    i = 1
    dat2 = open('trenutek1.txt',"w")
    for vrstica in datoteka:
        dat2.write(str(i) +","+ vrstica)
        i += 1
    dat2.close()
