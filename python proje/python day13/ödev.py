ad = input("Adınız: ")
kilo = int(input("Kilonuz: "))
boy = int(input("Boyunuz: "))

indeks = kilo/(boy**2)*10000

if 30 < indeks < 34.9:
    print("Sayın ", ad, " Kilo indeksi: ", indeks, "=> Şişman")
elif 25 < indeks < 29.9:
    print("Sayın ", ad, " Kilo indeksi: ", indeks, "=> Fazla kilolu")
elif 18.5 < indeks < 24.9:
    print("Sayın ", ad, " Kilo indeksi: ", indeks, "=> Normal")
else:
    print("Sayın ", ad, " Kilo indeksi: ", indeks, "=> Zayıf")
