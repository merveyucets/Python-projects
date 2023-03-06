#"Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın."

vize1=int(input("1.vize notunuz: "))
vize2=int(input("2.vize notunuz: "))
final=int(input("Final notunuz: "))

ortalama=(vize1 + vize2)*0.6 + final*0.4

if ortalama>=50:
    print("Ortalamanız: ",ortalama," Tebrikler, geçtiniz.")
else:
    print("Ortalamanız: ",ortalama," Üzgünüz, kaldınız.")