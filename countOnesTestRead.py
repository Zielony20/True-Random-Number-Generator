import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
import math

def Phi(x):
{
  tmp = x/np.sqrt(2.)
  tmp = 1+math.erf(tmp) 

  return tmp/2
}


words_file = open("slowa.txt",'r')
Q5=[]
Q4=[]

for q in range(100):
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
    
    wordsCounter = dict(sorted(wordsCounter.items()))
    mean = 0
    Q = 0
    f_exp = []
    to_display = []
    for v,k in wordsCounter.items():
        mean = np.prod([propability[i] for i in v ]) * sum_latter_number
        f_exp.append(mean)
        #print(mean)
        observ = k
        Q += ((k-mean)**2)/mean
        to_display.append(k)
    Q5.append(Q)
    #print(Q)
    #print(len(wordsCounter))
    plt.plot( np.linspace(1, 3125,num=3125),to_display)
    
    plt.savefig("5-words_distribution.png")
    plt.clf()
    plt.cla()
    plt.close()
    
    t=[]
    for i,j in wordsCounter.items():
        t.append(j)

    chisq, p = scipy.stats.chisquare( t ,f_exp = f_exp)
    print("Słowa 5-literowe: ",chisq, p)
words_file.close()


words_file = open("slowa.txt",'rt')
for q in range(100):

    
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
    


    
    wordsCounter = dict(sorted(wordsCounter.items()))
    Q=0
    f_exp = []
    to_display = []
    for v,k in wordsCounter.items():
        mean = np.prod([propability[i] for i in v ]) * sum_latter_number
        f_exp.append(mean)
        #print(mean)
        observ = k
        Q += ((k-mean)**2)/mean
        to_display.append(k)
    Q4.append(Q)
    #ABCDEAB
    plt.plot( np.linspace(1, 625,num=625),to_display)
    
    plt.savefig("4-words_distribution.png")
    plt.clf()
    plt.cla()
    plt.close()
    
    #print(Q4)
    #print(len(wordsCounter))
    t=[]
    for i,j in wordsCounter.items():
        t.append(j)

    chisq, p = scipy.stats.chisquare( t ,f_exp = f_exp)
    print("Słowa 4-literowe: ",chisq, p)
words_file.close()

#print(Q4)

plt.plot( np.linspace(1, 100,num=100),Q4)
    
plt.savefig("Q4.png")
plt.clf()
plt.cla()
plt.close()

plt.plot( np.linspace(1, 100,num=100),Q5)
    
plt.savefig("Q5.png")
plt.clf()
plt.cla()
plt.close()
Qdiff = np.array(Q5)-np.array(Q4)
plt.plot( np.linspace(1, 100,num=100) , Qdiff )
    
plt.savefig("Q5-Q4.png")
plt.clf()
plt.cla()
plt.close()


mean=2500 
std=np.sqrt(5000)

p_value_Q_differ = 1-Phi((Qdiff-mean)/std)
plt.plot( np.linspace(1, 100,num=100) , p_value_Q_differ )
    
plt.savefig("Pvalue_Q5-Q4.png")
plt.clf()
plt.cla()
plt.close()

p_value_Q5 = 1-Phi((np.array(Q5)-mean)/std)
plt.plot( np.linspace(1, 100,num=100) , p_value_Q5 )
    
plt.savefig("Pvalue_Q5.png")
plt.clf()
plt.cla()
plt.close()

p_value_Q4 = 1-Phi((np.array(Q4)-mean)/std)
plt.plot( np.linspace(1, 100,num=100) , p_value_Q4 )
    
plt.savefig("Pvalue_Q4.png")
plt.clf()
plt.cla()
plt.close()


