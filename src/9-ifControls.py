# ==========================================
#                 ifControls
# ==========================================

x = 5
y = 2
print(x > y) # True Çıktısını Verecektir.
print(x < y) # False Çıktısını Verecektir.

print(x >= y) # True Çıktısını Verecektir
print(x <= y) # False Çıktısını Verecektir

print(x >= 5.0) # True Çıktısını Float'a Karşın Yine Verecektir.
print(x >= 5.01) # False Çıktısını Verecektir

x = 10
y = 8
x = y # x'in Değerini y Olarak Değiştir
x = 10

print(x == y) # x y'ye Eşit Değilse False Döndürecektir
print(x != y) # x y'ye Eşit Değilse True Döndürecektir

# AND Bağlacı

print(2 > 1 and 3 > 2) # İki Koşul Da Doğru Olduğundan True Çıktı True Döncektir.
print(2 > 4 and 3 > 4) # İki Koşul Da Ve Bağlacında False Değer Döndürüyorsa Direkt False'dır.
print(2 > 0 and 3 < 2) # İki Koşuldan Birisi False Birisi True Olsa Bile Ve Bağlacında Çıktı False Döndürecektir.

print(True and True) # ---> True = 1
print(True and False) # ---> False = 0
print(False and False) # ---> False = 0

# OR Bağlacı

print(2 > 1 or 3 < 2)  # İki Koşuldan Biri Doğruysa Veya Bağlacında, Çıktı True Döner.
print(2 > 4 or 3 > 4) # İki Koşuldan İkisi De False İse Çıktımız False Olarak Dönecektir
print(2 > 0 and 3 < 5) # İki Koşulda Doğruysa Sonuç True Dönecektir.

# NOT Bağlacı

print(not 1 == 1) # Normalde True Dönecek Bir Karşılaştırma 'not' Eki Yüzünden False Dönüyor.

# İN Kontrolcüsü

print(10 in (10,20,30))
print(10 in [10,20,30]) # 'in' Fonksiyonu Bir Listenin İçerisinde Belirtilen Parametrenin Olup Olmadığı Çıktısını Döndürür.
print(5 in [3,6,7])

print(3 not in [3,6,7]) # 3 Sayısı Listede Olduğundan False Olarak Dönecek
print(2 not in [3,6,7]) # 2 Sayısı Listede Olmadığı İçin True Olarak Dönecektir.

print("Talha" in ["Talha", "Arda", "Ahmet"]) # Aynı Şekilde Stringlerde de Oluyor; Büyük Harf Küçük Harf Önemli!!

my_dictionary = {"a":1, "b":2, "c":3}
print(1 in my_dictionary) # Sözlüklerde 'in' Bu Şekilde Değil
print(1 in my_dictionary.values()) # Bu Şekilde Çalışmaktadır.
print("b" in my_dictionary.keys())

my_Superhero = "Kratos"
print(my_Superhero == "Kratos") # Eğer Değişkende Belirlediğin String Eşitlenmeye Çalışılan String Değeriyle Aynı ise True Dönecektir

# IF Controller

if my_Superhero == "Kratos":
    print("Kratos") # Yukarıdaki İf Kontrolümüz True Olarak Dönerse Bu Veya Altına Eklenen Kodlar Çalışacaktır.
#########------------############ ---> İf Bloğunun Bittiği Satır

# Multi IF Controller

my_superhero = input("Enter Superhero: ")

if my_superhero == "Superman":
    print("Superman")
elif my_superhero == "Kratos":
    print("Kratos")
elif my_superhero == "Batman":
    print("Batman")
elif my_superhero == "Ironman":
    print("Ironman")
else:                                           # Else ise Değilse, Yoksa Anlamında ve Fonksiyonunda Kullanılır
    print("The Superhero is not recognized")


myAge = 19

if myAge <= 18:
    print("age <= 18")
elif myAge > 18 and myAge <= 30:
    print("18 < age < 30")
elif myAge > 30 and myAge <= 40:
    print("30 < age < 40")
else:
    print("age > 40")


my_superhero = input("Enter Superhero: ")
my_superhero_list = ["Spider Man", "Iron Man", "Thor", "Hulk", "Black Widow"]

if my_superhero in my_superhero_list:
    print(" :) ")
else:
    print(" :( ")











