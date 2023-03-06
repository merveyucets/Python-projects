# "Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz. (email: email@ytubmk.com - parola:abc123)"

bilgi = {"email": "email@ytubmk.com", "parola": "abc123"}

email = input("Mail adresinizi yazınız: ")

if email == bilgi["email"]:
    parola = input("Parolanızı giriniz: ")
    if parola == bilgi["parola"]:
        print("Giriş başarılı")
    else:
        print("Parolanız yanlış.")
else:
    print("Mail adresiniz yanlış.")
