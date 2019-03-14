
#DYNAMİC YÖNTEM->çalışması uzun sürüyor.
def recMC(coinValueList,change):
  minCoins=change
  if(change in coinValueList):
    return 1
  else:
    for i in [c for c in coinValueList if c<=change]:
      numCoins=1+recMC(coinValueList,change-i)
      if(numCoins<minCoins):
        minCoins=numCoins
  return minCoins
print(recMC([1,5,10,25,50],30))

#İyileştirilmiş hali
def recMC(coinValueList,change,knownResults):
  minCoins=change
  if(change in coinValueList):
    knownResults[change]=1
    return 1
  elif(knownResults[change]>0):
    return knownResults[change]
  else:
    for i in [c for c in coinValueList if c<=change]:
      numCoins=1+recMC(coinValueList,change-i,knownResults)
      if(numCoins<minCoins):
        minCoins=numCoins
        knownResults[change]=minCoins
  return minCoins
print(recMC([1,5,10,21,25,50],63,[0]*64))


#Başka çözüm..
def para_ustu(n):
  tut=n
  kullanilan_para1=[]
  kullanilan_para2=[]
  liste=[1,5,10,21,25,50]
  k=len(liste)-1
  m=len(liste)-1
  r=0
  z=0
  while(m>=0):
    if(tut%liste[m]==0):
      for i in range(tut//liste[m]):
        kullanilan_para1.append(liste[m])
        r+=1
      
      break
    else:
      m-=1
  
  
  while(k>=0):
      if(liste[k]<=n):
        kullanilan_para2.append(liste[k])
        n=n-liste[k]
        z+=1
      else:
        k-=1

  if(z>r):
    return kullanilan_para1
  return kullaniülan_para2
        
print(para_ustu(63))


