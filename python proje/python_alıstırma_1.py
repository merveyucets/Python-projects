
names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]


names.append("Cenk")   # 1-"Cenk" ismini listenin sonuna ekleyiniz.
print(names)

names.insert(0,"Sena")   # 2-"Sena" değerini listenin başına ekleyiniz.
print(names)

names.remove("Deniz")   # 3-"Deniz" ismini listeden siliniz.
print(names)

names.insert(3,"Deniz")    # 4-"Deniz" isminin indeksi nedir ?
print(names.index("Deniz"))

if "Ali" in names:  # 5-"Ali" listenin bir elemanı mıdır ?
    print(True)
else:
    print(False)

names.reverse()   # 6-Liste elemanlarını ters çevirin.
print(names)

names.sort()   # 7-Liste elemanlarını alfabetik olarak sıralayınız.
print(names)

years.sort()   # 8-years listesini rakamsal büyüklüğe göre sıralayınız.
print(years)

str="Chevrolet,Dacia"   # 9-str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str=list(str.split(","))
print(str)

max_number= years[0]   # 10-years dizisinin en büyük ve en küçük elemanı nedir ?
min_number= years[0]
for i in years:
    if i>=max_number:
        max_number=i
    else:
        min_number=i
print("en büyük sayı: ",max_number,"en küçük sayı: ", min_number)

sayac=0          # 11-years dizisinde kaç tane 1998 değeri vardır ?
for i in years:
    if i==1998:
        sayac=sayac+1
print(sayac)

for i in range(len(years)):   # 12-years dizisinin tüm elemanlarını siliniz.
    years.pop()
print(years)

marka=[]   # 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
for i in range(3):
    x=input("tercih ettiğiniz markayı yazar mısınız: ")
    marka.append(x)
print(marka)











