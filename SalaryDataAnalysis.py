# Maaş Analizi Örneği
import numpy as np

print("Hikaye şu şekilde: Aşağıda 50 kişinin maaş listesi bulunmaktadır. Maaşlar 17_500-45_000 aralığında olması gerekiyor.")
print("Aykırı maaşlar, en yüksek/en düşük maaşlar, yüksek maaşlı çalışanlar(30.000 ve üzeri) tespit ediliyor ve maaş ortalamaları, standart sapma, meydan varyans hesaplanıyor...")

# Maaş Listesi
maaslar = np.random.randint(15_000,55_000,50)
print(f"Maaşlar şu şekildedir: {list(maaslar)}")

# Aykırı maaşları bulma ve kaç kişi olduğunu tespit etme
aykiriKosulu = (maaslar < 17_500) | (maaslar > 45_000)
aykiriMaaslar = maaslar[aykiriKosulu]
aykiriMaasListesi = list(aykiriMaaslar)
print(f"Aykırı maaş listesi: {aykiriMaasListesi}")
print(f"Aykırı maaş sayısı: {len(aykiriMaasListesi)}")

# Listeden çıkartma işlemi 
temizlenmisMaaslar = maaslar[~aykiriKosulu]
temizlenmisMaaslarListesi = list(temizlenmisMaaslar)
print(f"Aykırı maaşlar çıkarıldıktan sonra maaşlar: {temizlenmisMaaslarListesi}")

# En yüksek ve en düşük maaş
temizlenmisMaaslarMax = temizlenmisMaaslar.max()
print(f"En yüksek maaş: {temizlenmisMaaslarMax} TL")

temizlenmisMaaslarMin = temizlenmisMaaslar.min()
print(f"En düşük maaş: {temizlenmisMaaslarMin} TL")

# 30_000 TL üzerinde maaş alan kişi sayısı
cokMaasAlanlar = temizlenmisMaaslar[temizlenmisMaaslar > 30_000]
print(f"30.000 TL üzeri maaş alan kişi sayısı: {len(cokMaasAlanlar)}")

# Ortalama, medyan, varyans, standart sapma hesaplamaarı
temizlenmisMaaslarOrt = np.mean(temizlenmisMaaslar)
print(f"Maaş ortalaması: {temizlenmisMaaslarOrt:.2f}")

siraliMaaslar = np.sort(temizlenmisMaaslar)
print(f"Sıralı maaş listesi(artan): {list(siraliMaaslar)}")

temizlenmisMaaslarMedyan = np.median(siraliMaaslar)
print(f"Medyan maaş: {temizlenmisMaaslarMedyan:.2f} TL")

temizlenmisMaaslarVaryans = np.var(temizlenmisMaaslar)
print(f"Maaşların varyansı: {temizlenmisMaaslarVaryans:.2f}")

temizlenmisMaaslarStdSapma = np.std(temizlenmisMaaslar)
print(f"Maaşların standart sapması: {temizlenmisMaaslarStdSapma:.2f}")

