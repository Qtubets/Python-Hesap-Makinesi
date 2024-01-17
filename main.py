ilkislem = int(input("İlk Sayıyı Giriniz "))
ikinciislem = int(input("İkinci Sayıyı Giriniz "))
islem = input("""Yapmak İstediğiniz İşlemi Giriniz.
(Toplama:+, Çıkarma:-, Çarpma:*, Bölme:/)
""")

if islem == "+":
    print("Sonuç: " +str(ilkislem+ikinciislem))

elif islem == "-":
        print("Sonuç: " + str(ilkislem - ikinciislem))

elif islem == "*":
            print("Sonuç: " + str(ilkislem * ikinciislem))

elif islem == "/":
                print("Sonuç: " + str(ilkislem / ikinciislem))

else:
                print("Geçersiz işlem! Lütfen doğru bir işlem seçin.")
