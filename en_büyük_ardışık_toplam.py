#Listedeki ardışık olarak elemanları topla
  #Ardışık olarak bulunan en büyük toplamı ve toplam listesinı ekrana bastır.

def max_bul(n):
  max_list=[]
  k=0
  a=len(n)#6
  while(len(n)>k):
    toplam=n[k]
    for i in range(k+1,a):# 0-1 , 0-1-2-3 ,
      toplam+=n[i]
      max_list.append(toplam)
    k+=1

  en_buyuk=max_list[0]
  for i in range(len(max_list)):
    if(en_buyuk<max_list[i]):
      en_buyuk=max_list[i]
   
  print("en büyük toplam = ",en_buyuk, "\n")
  return max_list

result=[-1,-2,3,4,5,6]
print(max_bul(result))
