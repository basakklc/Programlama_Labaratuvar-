#Text.txt dosyasının içeriği 

	#Programlama Labaratuvarı Dosya okuma kodu için hazırlanan text .

class myClass():
    def __init__(self,myFile='.'):
        f=open("text.txt","r")
        myContent=f.read()
        mySentences=myContent.split()
        self.myWords=[]
        for sentence in mySentences:
            Words_In_the_Sentence=sentence.split(" ")
            for word_1 in  Words_In_the_Sentence:
                self.myWords.append(word_1)

    
    def my_frequency_1(self):
        self.frequency_list_1={}
        for word in self.myWords:
           if(word in self.frequency_list_1):
               self.frequency_list_1[word]+=1
           else:
               self.frequency_list_1[word]=1

    def write_frequency_1(self):
        for word_1 in self.frequency_list_1:
            print(word_1+ " "+str(self.frequency_list_1[word_1]))##
    
    def my_frequency_2(self):
        self.frequency_list_2={}
        for i in range(len(self.myWords)-1):
            w_1,w_2=self.myWords[i],self.myWords[i+1]
            if((w_1,w_2) in self.frequency_list_2):
               self.frequency_list_2[(w_1,w_2)]+=1
            else:
               self.frequency_list_2[(w_1,w_2)]=1
 

    def write_frequency_2(self):
        for w_2 in self.frequency_list_2:
            print(str(w_2)+ " "+str(self.frequency_list_2[w_2]))




my_Class_1=myClass()
print(len(my_Class_1.myWords))

my_Class_1.my_frequency_1()
my_Class_1.write_frequency_1()
print(my_Class_1.frequency_list_1['Dosya'])

