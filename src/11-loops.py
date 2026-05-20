# ==========================================
#                   LOOPS
# ==========================================

#for loop, while loop

# --For Loop--
my_List = [10,20,30,40,50,60,70,80,90]
print(my_List[0] / 5 * 2)
print(my_List[-1] / 5 * 2)

for num in my_List:
    print(num) # Liste İçerisindeki Tüm Değerleri Yazdırır

print("For Loop Started") # Döngü Başlatılıyor
for x in my_List:
    new_number = (x / 5) * 2 # Listedeki Değerleri 5'e Böl Sonra 2 İle Çarp
    print(new_number)
print("For Loop Ended") # Döngü Bitiriliyor

for y in my_List:
   if y % 6 == 0: # Listede Yalnızca 6'ya Bölünenleri Sırala
       print(y)

numberList = [0,1,2,3,4,5,6,7,8,9,10,11,12]

for a in numberList:
    if a % 2 == 0: # Çift Sayıları Yazdıran Bir Döngü
        print(a)

for a in numberList:
    if a % 2 != 0: # Tek Sayıları Yazdıran Bir Döngü
        print(a)

myString = "Talha Gumuskaya"

for c in myString:
    print(c) # Tüm Karakterleri Tek Tek Sıralıyor

myTuple = (1,2,3,4,5,6,7,8,9,10)

for num in myTuple:
    print(num)
    print(num / 5 * 2)

my_new_list = [("a","b"),("c","d"),("e","f"),("g","h")]
print(my_new_list[0])

for element in my_new_list:
    print(element) # Tüm Tuple'ları Sıra Sıra Verir

    # Tuple Unpacking
for (x,y) in my_new_list:
    print(x) # Notasyona Uyan Kısımdaki Değerleri Getirir

my_tuple_list = [(0,1,2),(3,4,5),(6,7,8),(9,10,11),(12,13,14)]

for (x,y,z) in my_tuple_list:
    print(x)

my_set = {1,2,3,4,5,6,7,8,9,10}

for num in my_set:
    print(num) # Setlerde De Aynı Şekilde Çalışıyor.

my_dict = {"k1":100,"k2":200,"k3":300}

for element in my_dict.items(): # İtems Fonksiyonu Sayesinde
    print(element) # Anahtar-Değer Verilerini Verir

for element in my_dict.values(): # Values Fonksiyonu Sayesinde
    print(element) # Sadece Değer Verilerini Verir

    # continue - break - pass

    my_List = [1,2,3,4,5,6,7,8,9,10]

print("for loop started")
for num in my_List:
    print(num)
print("for loop ended")

# -- break --
for num in my_List:
    print(num)
    if num == 5:
        print("The number is 5") # Eğer Break Eklemeseydik 5'ten Sonra Sıralamaya Devam Edicek
        break # Break Eklediğimiz İçin Aradığımız Yerden Sonra Döngüyü Kırdı

# -- continue --

my_list = [10,20,30,40,50,60,70,80,90]

for number in my_list:
    if number != 40: #
        print(number)
        continue # Döngüyü Belirli Bir Yere Kadar Devam Ettirir

# -- pass --

for number in my_list:
    pass # Kod Geliştirilirken Geriye Dönük Kullanılır

# --While Loop--

x = 0

print("while loop started")
while x < 10: # x 10'dan Küçük Olana Kadar Döngüyü Devam Ettir
    print(x) # Infinity Loop
    x += 1 # 10'dan Küçük Olana Kadar Kontrollü Bir Şekile 1 Ekleyerek Döngüye Sok
print("while loop ended")

last_list = [10,20,30,40,50,60,70,80,90]

while 20 in last_list:
    print("20 in last_list")
    last_list.pop()

# -- formatted string --
my_list = [10,20,30]
print(my_list)
print(f"my list: {my_list}") # 'f' --> Formatlar

name = input("Please enter your name: ")
print(f"Hello {name}, welcome to Python")

print("Welcome", name) # Alternatif Kullanım

p = 0
while p < 20: # 'p' 20'den Küçük Olduğu Sürece Programımız Dönsün
    print(f"value of p:{p}")
    p += 1 # Her Seferinde 'p' Değerini 1 Arttır

    


