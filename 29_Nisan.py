import random 
def get_n_random_integer(n):
  random.seed(100)
  numbers = []
  for i in range(n):
    s = random.randint(-100,100)
    numbers.append(s)
  return numbers

def get_mean_for_n_integer(numbers):
  toplam = 0
  kactane = 0
  for sayi in numbers : 
    toplam = toplam+sayi
    kactane =kactane+1

  
  return toplam/kactane


def get_std_for_n_integer(numbers):
  toplam = 0
  kactane = 0
  ortalama = get_mean_for_n_integer(numbers)
  for sayi in numbers : 
    toplam = toplam+(sayi-ortalama)**2
    kactane =kactane+1

  var_1 = toplam/(kactane-1)  
  std_1 = var_1**.5
  return std_1

def normalizasyon(numbers):
  new_numbers = []
  ortalama = get_mean_for_n_integer(numbers)
  standart_sapma = get_std_for_n_integer(numbers)

  for x in numbers:
    new_x = (x-ortalama)/standart_sapma
    new_numbers.append(new_x)

  return new_numbers

def get_mean_one_std_neigbor_ratio(numbers):
  kactane = 0
  toplamKacSayi = 0
  ortalama = get_mean_for_n_integer(numbers)
  standartd_sapma=get_std_for_n_integer(numbers)

  low = ortalama-standartd_sapma
  high = ortalama+standart_sapma
  for x in numbers:
    toplamKacSayi = toplamKacSayi+1
    if(x>low and x<high):
      kactane = kactane+1
  return  kactane/toplamKacSayi



def insertion(numbers):
    sayilar_2 = numbers
    length_1 = len(sayilar_2)
    for i in range(1,length_1):
        for j in range(i,0,-1):
            if(sayilar_2[j]<sayilar_2[j-1]):
                temp = sayilar_2[j-1]
                sayilar_2[j-1] = sayilar_2[j]
                sayilar_2[j] = temp
    return sayilar_2
  
sayilar = get_n_random_integer(5)
ortalama = get_mean_for_n_integer(sayilar)
standart_sapma = get_std_for_n_integer(sayilar)
yeni_sayilar = normalizasyon(sayilar)

print("sayilar = ",sayilar)
print("ortalama = ",ortalama)
print("standart sapma = ",standart_sapma)
print("yeni normalize edilmiş liste = ",yeni_sayilar)

sayilar_1 = get_n_random_integer(100)
print(get_mean_one_std_neigbor_ratio(sayilar_1))
print(yeni_sayilar)
