# ==========================================
#                DICTIONARY
# ==========================================

# key - value pairing / anahtar - değer eşleşmesi

fruitList = ["apple", "banana", "cherry"]
calorieList = [60, 70, 80]

print(fruitList[0]) # Elmayı Seçtiğimizde
print(calorieList[0]) # Aynı Şekilde Kaloriyi De Seçmemiz Gerekir Ama Bu Çok Sağlıklı Bir Yöntem Değil.

fitnessDictionary = {"apple":60, "banana":70, "cherry":80} # Sözlüğü Oluşturduğumuz Satır
print(type(fitnessDictionary)) # Göründüğü Gibi Veri Tipi 'Dictionary' Oldu.

# print(fitnessDictionary[0]) --> Sözlüklerde İndeks Mantığı Yoktur Anahtar-Değer Eşleşmesi Kullanılır.
print(fitnessDictionary["apple"])
print(fitnessDictionary["banana"]) # İndeks Yerine İsim Girilmelidir.
print(fitnessDictionary["cherry"])

print(fitnessDictionary.keys()) # Sözlükteki Anahtarları Veriyor.
print(fitnessDictionary.values()) # Sözlükteki Anahtarlara Atanmış Değerleri Veriyor.

fitnessDictionary["apple"] = 80 # Atanan Değeri Anahtarı Çağırıp Değiştirebiliyoruz.

fitnessDictionary["melon"] = 120 # Sözlüğe Sonradan Anahtar-Değer Ekleme Yöntemi.
print(fitnessDictionary)

myDictionary = {100:"a", 200:"b", 300:"c"} # Sözlüklerde İkinci Girilen Değer Her Zaman Değerdir.
print(myDictionary[100]) # Bu Seferde Anahtarımız Integer Değerimiz String

myDictionary = {"key1":"value1", "key2":"value2", "key3":"value3"} # Hem Anahtar Hem Değer String Olabilir
print(myDictionary["key1"])

myMixedDictionary = {"key1":100, "key2":3.14, "key3":[10,20,30]} # Bir Sözlük İçerisine Farklı Veri Tipleri Alınabilir
print(myMixedDictionary["key1"]) # Integer Değerini Verdi
print(myMixedDictionary["key2"]) # Float Değerini Verdi
print(myMixedDictionary["key3"]) # Liste Değerini Verdi

print(myMixedDictionary["key3"][1]) # Sözlüğümüzdeki Liste Değerinin İçindeki Sayıyı İndeksleyerek Alabiliriz

lasDictionary = {"k1":10, "k2":[10,20,30,40,50], "k3":"string", "k4":{"a":100, "b":200, "c":300}}
print(lasDictionary["k4"]["b"]) # Sözlük İçindeki Sözlüğümüzden Bir Değer Aldık :D
print(lasDictionary["k2"][3]) # Sözlük İçindeki Listemizin İçerisinden 3. İndeksle 40 Sayısını Aldık





