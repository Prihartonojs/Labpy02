Bilangan1 = int(input("Masukan Bilangan 1:"))
Bilangan2 = int(input("Masukan Bilangan 2:"))
Bilangan3 = int(input("Masukan Bilangan 3:"))

if  int(Bilangan1) and Bilangan1 > Bilangan3:
    print("Nilai Terbesarnya adalah :", Bilangan1)
    Tersabar = Bilangan1
    NomBil = "Bilangan 1"
elif (Bilangan2 > Bilangan3) and (Bilangan2 > Bilangan1):
    print("Nilai tersebar adalah :", Bilangan2)
    Terbesar = Bilangan2
    NomBil = "Bilangan 2"
else:
    Terbesar = Bilangan3
    NomBil = "Bilangan 3"

    print("Bilangan yang terbesar adalah", Bilangan1, "dengan nilai", Terbesar)