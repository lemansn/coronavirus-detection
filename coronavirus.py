nufus = int(input('Şehirde yaşayan insan sayısını giriniz: '))
olgu = int(input('Testler sonucunda saptanan olgu sayısını giriniz: '))
hasta = int(input('Toplam hasta sayısını giriniz: '))


TESTIN_MAILIYETI = 125
HAFIF_HASTA_TEDAVISI = 1250
AGIR_HASTA_TEDAVISI  = 12500

#Olgu sayısının nüfusa oranı
olgu_nufus_oran = (olgu/nufus) * 100

#Hastalık belirtisi vermeyen olgu sayısı
bel_olmayan_olgu = olgu-hasta

#Hastalık belirtisi vermeyen olguların tüm olgular içindeki oranı
bel_olmayanin_tum_olguya_orani = (bel_olmayan_olgu / olgu) * 100

#Süreç boyunca karşılaşılacak yaklaşık ağır hasta sayısı
agir_hasta = round(hasta * 0.15)

#Süreç boyunca karşılaşılacak yaklaşık ölüm sayısı
olum_sayi = round(hasta * 0.02)

#Hastalığın şehir bütçesine getireceği yaklaşık toplam maliyet
toplam_maliyet = nufus * TESTIN_MAILIYETI + agir_hasta * AGIR_HASTA_TEDAVISI + (hasta - agir_hasta) * HAFIF_HASTA_TEDAVISI

#Hastalığın tüm nüfus dikkate alındığında yaklaşık kişi başı ortalama maliyeti
kisi_basi_maliyet = toplam_maliyet / nufus

print(f'Olgu sayısının nüfusa oranı: %{format(olgu_nufus_oran,".3f")}')
print("Hastalık belirtisi vermeyen olgu sayısı:",bel_olmayan_olgu)
print(f'Hastalık belirtisi vermeyen olguların tüm olgular içindeki oranı: %{format(bel_olmayanin_tum_olguya_orani,".3f")}')
print("Süreç boyunca karşılaşılacak yaklaşık ağır hasta sayısı:",agir_hasta)
print("Süreç boyunca karşılaşılacak yaklaşık ölüm sayısı:",olum_sayi)
print("Hastalığın şehir bütçesine getireceği yaklaşık toplam maliyet:",format(toplam_maliyet,',d'),"TL")
print("Hastalığın tüm nüfus dikkate alındığında yaklaşık kişi başı ortalama maliyeti:",format(kisi_basi_maliyet,'.2f'),"TL")





