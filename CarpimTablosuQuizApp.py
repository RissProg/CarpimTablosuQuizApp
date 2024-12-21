from random import randint

"""
     Carpim Tablosu Uygulamasi
"""
print("-" * 50)
print("\t\tHOSGELDINIZ..")
print("-" * 50, "\n")

def carpim(i, j, r):
    if r != "-1":
        result = str(i * j)
        if result == r:
            print("\t\t***** Dogru *****")
        else:
            print("\t!!! Yanlis Cevap, dogru cevap: %s" % result)
    else:
        secim()

def basla(range_1, range_2):
    if range_1 > 10:
        x = 10
    else:
        x = 5
    for i in range(0, x):
        for j in range(0, x):
            s1 = randint(range_1, range_2)
            s2 = randint(range_1, range_2)
            print("_" * 50, "\n")
            print("\t%d x %d kac eder ? (cikis = -1)" % (s1, s2))
            sonuc = input("Sonuc: ")
            carpim(s1 , s2 , sonuc)  

            if i == 4 and j == 4:
                print("\n *-- Bu Bolum Bitti, Bir Ust Bolume Gecebilirsiniz --*\n")
                secim()

def secim():
    print("Hangi Seviyeden Baslamak Istersiniz (cıkis = -1) ?\n")
    print(" 1 > Kolay ")
    print(" 2 > Orta ")
    print(" 3 > Zor ")
    print(" 4 > Çok Zor ")

    seviye = input(" >> ")

    if seviye == "1":
        basla(1, 6)
    elif seviye == "2":
        basla(6, 12)
    elif seviye == "3":
        basla(12, 25)
    elif seviye == "4":
        basla(25, 100)
    elif seviye == "-1":
        exit(0)  

if __name__ == "__main__":
    secim()
