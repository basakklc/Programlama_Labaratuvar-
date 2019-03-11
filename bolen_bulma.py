#asal çarpanlara ayırma kodu..
  #asal sayı ise asal yazsın, değilse bölenlerini ekrana yazsın.
def carpan_bul(n):
  result=[]
  i=2
  while(i<=n):
    if(n%i!=0):
      i+=1
      continue
    result.append(i)
    n=n//i
    i+=1
  if(len(result)==1):
    print("asal sayıdır")
  return result

print(carpan_bul(105))
