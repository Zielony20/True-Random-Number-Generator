import scipy.stats
import numpy as np


words_file = open("slowa.txt",'rt')
wordsCounter={'AAAAA':0}

propability={
    'A':37/256,
    'B':56/256,
    'C':70/256,
    'D':56/256,
    'E':37/256
}
sum_latter_number = 256000
i=0
word=''
for letter in words_file:
    
    word+=letter[0]
    if(len(word)==5):
        i+=1 # mamy pierwsze słowo
        if(word in wordsCounter.keys()):
            wordsCounter[word]+=1
        elif(word not in wordsCounter.keys()):
            #print("nie ma ",word, " w ",wordsCounter.keys())
            wordsCounter[word]=1
        
        word=word[1:]
    if(i>=256000):
        break
words_file.close()

#print(wordsCounter)
print( )
mean=0
Q5=0
f_exp=[]
for v,k in wordsCounter.items():
    mean = np.prod([propability[i] for i in v ]) * sum_latter_number
    f_exp.append(mean)
    #print(mean)
    observ = k
    Q5 += ((k-mean)**2)/mean

print(Q5)
#print(len(wordsCounter))
t=[]
for i,j in wordsCounter.items():
    t.append(j)

chisq, p = scipy.stats.chisquare( t ,f_exp = f_exp)
print("Słowa 5-literowe: ",chisq, p)



words_file = open("slowa.txt",'rt')
wordsCounter={'AAAA':0}
i=0
word=''
for letter in words_file:
    word+=letter[0]
    if(len(word)==4):
        i+=1 # Mamy słowo licznik +1
        if(word in wordsCounter.keys()):
            wordsCounter[word]+=1
        elif(word not in wordsCounter.keys()):
            #print("nie ma ",word, " w ",wordsCounter.keys())
            wordsCounter[word]=1
        
        word=word[1:]
    if(i>=256000):
        break
words_file.close()


#print(wordsCounter)

Q4=0
f_exp = []
for v,k in wordsCounter.items():
    mean = np.prod([propability[i] for i in v ]) * sum_latter_number
    f_exp.append(mean)
    #print(mean)
    observ = k
    Q4 += ((k-mean)**2)/mean


print(Q4)
print(len(wordsCounter))
t=[]
for i,j in wordsCounter.items():
    t.append(j)


chisq, p = scipy.stats.chisquare( t ,f_exp = f_exp)
print("Słowa 4-literowe: ",chisq, p)







