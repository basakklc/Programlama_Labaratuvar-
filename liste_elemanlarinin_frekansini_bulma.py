#kendisine aktarılan listenin frekans tablosunu bulup geri döndüren fonksiyon...

my_list=[2,3,5,8,2,4,3,3,2,8,5,2]
a=[2,3] #liste
b=(2,3) #tuppel veri değiştirilmez ama perfonması iyidir.
c={2:3} #sözlük->anahtar=2, frekansı=3 


#sözlük ile..
my_list=[2,3,5,8,2,4,3,3,2,8,5,2]
def my_freq(list):
  freq_dict={}#sözlük..
  for i in list:
    if(i in freq_dict):
      freq_dict[i]=freq_dict[i]+1
    else:
      freq_dict[i]=1
  return freq_dict

print(my_freq(my_list))  

#liste ile..
def freq_list(list):
  result=[]
  for i in range(len(list)):
    a=False
    for j in range(len(result)):
      if(result[j][0]==list[i]):
        result[j][1]+=1
        a=True
    if(a==False):
      result.append([list[i],1])
  return result

print(freq_list(my_list))  





