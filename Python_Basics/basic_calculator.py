def Topla(x, y):
    return x + y

def Cıkar(x, y):
    return x - y

def Carp(x, y):
    return x * y

def Bol(x, y):
    return x / y

print ("Yapılacak işlemi seçiniz.")
print ("(1) Toplama")
print ("(2) Çıkarma")
print ("(3) Çarpma")
print ("(4) Bölme")

secim = input("Seçiminiz (1/2/3/4):")

sayi1 = float(input("1. Sayıyı giriniz : "))
sayi2 = float(input("2. Sayıyı giriniz : "))

if secim == "1":
    print(Topla(sayi1,sayi2))

elif secim == "2":
    print(Cıkar(sayi1, sayi2))

elif secim == "3":
    print(Carp(sayi1, sayi2))

elif secim == "4" and sayi2 != 0:
    print(Bol(sayi1, sayi2))

else:
    print("Hatalı Giriş Yaptınız.")