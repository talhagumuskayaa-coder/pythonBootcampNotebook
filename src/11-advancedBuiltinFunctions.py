# ==========================================
#                   LOOPS
# ==========================================

# -- Range --

print(range(50)) # 0'dan Verdiğimiz Değere Kadar Aralık Belirtir: (0,50)
print(list(range(10))) # Berilenen Aralığı Verdiğimiz Değer Dahil Olmayacak Şekilde 0'dan İtibaren Sıralar.

for num in list(range(20)): # Örnek For Döngüsü Kullanımı
    print(num * 2)

print(list(range(5,25))) # Aralığı Statik Olarak Da Verebiliriz, Aynı Şekilde (x,y) Aralığındaki 'y' Dahil Değil.
print(list(range(5,25,2))) # örn(x,y,z): X'den Başlayarak Z'şer Atlayarak Sırala --> (5,7,9..,23)

my_list = [1,2,3,4]

for num in my_list:
    print(num) # Listedeki Tüm Değerleri Yazdırır

for ix in range(len(my_list)):
    print(ix) # İndeksleri Sıralar: 0,1,2,3
    print(my_list[ix]) # Listedeki İndeks Sırasına Karşılık Gelen Değeri İndeksiyle Beraber Çıktılar

# -- Enumerate --
for element in enumerate(my_list):
    print(element) # Tek Tek İndeks ve Değerlerini Tuple Olarak Çıktılar.

for (ix, value) in enumerate(my_list):
    print(value) # Listedeki İndeks Değerlerine Karşılık Gelen Değeri Çıktılar.

# -- Random --
from random import randint # 'random' Bir Kütüphane 'randint' İse O Kütüphanedeki Bir Fonksiyondur
print(randint(0,100)) # Belirlenen Aralıktan Random Bir Sayı Çıktılar

from random import shuffle # 'random' Kütüphanemizin İçindeki 'shuffle' da Aynı 'randint' Gibi Bir 'random' Kütüphane Fonksiyonudur
shuffle(my_list) # 'shuffle' Fonksiyonu Listemizin İçindeki Değerleri Karıştırıp Çıktılar
print(my_list)

my_list = [10,20,30,40,50,60,70,80,90]
print(randint(0,len(my_list))) # Listedeki Eleman Sayısına Göre Random Bir Sayı Çıktılayacak

print(my_list[randint(0,len(my_list))]) # Listede 9 Eleman Olduğundan Bize (0,9) Arası Bir Değer Çıktılayacak 0 ve 9'da Dahil.

# -- Zip --
food_list = ["Apple", "Banana", "Cherry", "Cheese", "Honey", "Sandwich"]
calories_list = [30,50,70,80,100,120]
day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Görüldüğü Gibi 3 Listemiz Ayrı Ayrı Durumlarda Fakat Hepsinin Bağlantısı Var

zipped_list = zip(food_list, calories_list, day_list) # 'zip' Fonksiyonu 3 Listemizi De Tek Bir Listeye Entegre Etti.
zipped_list = list(zipped_list)
print(zipped_list) # Hepsi Birer Tuple'ın İçerisinde Çıktılanır.

new_list = []
my_string = "Metallica"

for element in my_string:
    new_list.append(element)
print(new_list) # 'my_string' Değişkenimizdeki Tüm Harfler Bir Listede Ayrı Ayrı String Değerleri Halinde Çıktılandı.

# -- List Comprehension --
new_list = [element for element in my_string] # Yukardaki Formüle Göre Daha Kolaylaştırılmış Bir Alternatif
print(new_list)

number_list = [1,2,3,4,5,6,7,8,9]
new_number_list = [num for num in number_list]
print(new_number_list) # Yine 'number_list' Gelicek Fark Yok

new_number_list = [num/2 for num in number_list]
print(new_number_list) # Listeyi Yapılandırdığınız Parametreye Göre Çıktılıyor













