import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
import math
from tqdm import tqdm, trange

def Phi(x):

    tmp = x/np.sqrt(2.)
    tmp = 1+math.erf(tmp) 

    return tmp/2

file = 'slowaZGeneratora.txt'

words_file = open(file,'r')
Q5=[]
Q4=[]
N=100
for q in trange(N):
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
    #print("Słowa 5-literowe: ",chisq, p)
words_file.close()


words_file = open(file,'r')
for q in trange(N):

    
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
    for key,observ in wordsCounter.items():
        mean = np.prod([propability[i] for i in key ]) * sum_latter_number
        f_exp.append(mean)
        #print(mean)
        
        Q += ((observ-mean)**2)/mean
        to_display.append(observ)
    Q4.append(Q)
    
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
    #print("Słowa 4-literowe: ",chisq, p)
words_file.close()

#print(Q4)

plt.bar( np.linspace(1, len(Q4),num=len(Q4)),Q4)
    
plt.savefig("Q4.png")
plt.clf()
plt.cla()
plt.close()

plt.bar( np.linspace(1, len(Q5),num=len(Q5)),Q5)
    
plt.savefig("Q5.png")
plt.clf()
plt.cla()
plt.close()
Qdiff = np.array(Q5)-np.array(Q4)
plt.bar( np.linspace(1, len(Q5),num=len(Q5)) , Qdiff )
print('Mean Q5-Q4 =', np.mean(Qdiff))
plt.savefig("Q5-Q4.png")
plt.clf()
plt.cla()
plt.close()


mean=2500 
std=np.sqrt(5000)
p_value_Q_differ=[]
for i in Qdiff:
    p_value_Q_differ.append( 1-Phi((i-mean)/std) )

#plt.bar( np.linspace(1, len(p_value_Q_differ),num=len(p_value_Q_differ)) , p_value_Q_differ )
n, bins, patches = plt.hist(p_value_Q_differ)    
plt.savefig("Pvalue_Q5-Q4.png")
plt.clf()
plt.cla()
plt.close()

stats, p = scipy.stats.kstest(n,'uniform')
print(p)

p_value_Q5=[]
for i in Q5:
    p_value_Q5.append( 1-Phi((i-mean)/std) )


plt.bar( np.linspace(1, N,num=N) , p_value_Q5 )
    
plt.savefig("Pvalue_Q5.png")
plt.clf()
plt.cla()
plt.close()

p_value_Q4=[]
for i in Q4:
    p_value_Q4.append( 1-Phi((i-mean)/std) )

plt.bar( np.linspace(1,N,num=N) , p_value_Q4 )
    
plt.savefig("Pvalue_Q4.png")
plt.clf()
plt.cla()
plt.close()