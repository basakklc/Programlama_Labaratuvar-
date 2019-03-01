import random
def generate_an_array(n):
    my_array=[]
    for  i in range(n):
        s=random.randint(0,100)
        my_array.append(s)
    return my_array
my_arr_1=generate_an_array(10)
print(my_arr_1) 

def my_search_c(array_2,item):
  found=False
  for i in array_2:
    if(i==item):
      found =True
  return found


for i in range (len(my_arr_1)-1,0,-1):
  for j in range(i):
    if(my_arr_1[j]>my_arr_1[j+1]):
      t=my_arr_1[j]
      my_arr_1[j]=my_arr_1[j+1]
      my_arr_1[j+1]=t

print(my_arr_1)
print(my_search_c(my_arr_1,68))
