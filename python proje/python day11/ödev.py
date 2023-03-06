 #Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.

ogrenciler={}

kisiadet=int(input("Kayıt olacak öğrenci sayısı: "))

i=0
while i<kisiadet:
    print("Hoşgeldiniz :)")
    no=input("Öğrenci numaranız: ")
    ad=input("Adınız: ")
    soyad=input("Soyadınız: ")
    numara=input("Telefon numaranız: ")
    ogrenciler.update({
        no:{
        "Adı":ad,
        "Soyadı":soyad,
        "Telefon numarası":numara
        }
    })
    print("Kaydınız tamamlanmıştır.")
    i=i+1


#Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

no=input("Öğrenci numaranız: ")
ogrenci = ogrenciler[no]
print(ogrenci)

