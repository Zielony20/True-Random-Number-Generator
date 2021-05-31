'''
Sekwencja liczb 32-bitowych poddawana jest konwersji na liczby zmiennoprzecinkowe ⟨0,1).
Zaczynając od 𝑘 = 2
31 = 2147483647, test poszukuje liczby iteracji j niezbędnych do
zmniejszenia k z wartości początkowej do 1, przy zastosowaniu formuły 𝑘 = ⌈𝑘𝑓⌉, gdzie 𝑓
jest pobraną liczbą zmiennoprzecinkową. Dla 100 000 powtórzeń zliczona zostaje liczba wystąpień poszczególnych wartości j. Przypadki, w których 𝑗 < 6 zostają wliczone do stanu 6,
a 𝑗 > 48 wliczone do stanu 48. Uzyskany wektor wartości poddawany jest testowi chikwadrat
'''
import scipy.stats as sc
import numpy as np
import random
import matplotlib.pyplot as plt 
from tqdm import tqdm, trange
from trng import TrueRandomNumberGenerator


std=np.sqrt(84);
Ef=[21.03,57.79,175.54,467.32,1107.83, 2367.84,4609.44,8241.16,13627.81,20968.49,30176.12,40801.97,52042.03,62838.28,72056.37,78694.51,82067.55,81919.35,78440.08,72194.12,63986.79,54709.31,45198.52,36136.61,28000.28,21055.67,15386.52,10940.20,7577.96,5119.56,3377.26,2177.87,1374.39,849.70,515.18,306.66, 179.39, 103.24, 58.51, 32.69, 18.03,  9.82, 11.21];
Ef = np.array(Ef)/10  # fit to 100k numbers distribution
source = 'video1.mp4' 

T = TrueRandomNumberGenerator(source)


final_10_pvalue=[]

for r in range(10):
    resault=[]
    for i in trange(100000):
        
        k = 2147483647
        j=0
        while ( k!=1 and j<48 ):
            #f = np.random.rand(1)[0]
            f = T.rand(1,bits=32)/2**32
            k = np.ceil(np.multiply(k, f))
            j+=1
        if(j<6):
            j=6
        elif(j>48):
            j=48
        else:
            j=j
        resault.append(j)

    n,bins,patches=plt.hist( np.array(resault)-5, bins=43, range=[1,43] )
    plt.clf()
    plt.cla()
    plt.close()

    labels=np.linspace(1,len(Ef),num=len(Ef))
    x = np.arange(len(labels))
    fig, ax = plt.subplots()
    rects1 = ax.bar(labels, Ef, 0.35, label='Expected')
    rects2 = ax.bar(labels+0.35, n, 0.35, label='Observed')

    ax.set_title('')
    ax.legend()
    plt.savefig("squeez"+str(r)+".png")
    plt.clf()
    plt.cla()
    plt.close()


    chisq, p = sc.chisquare( n ,f_exp = Ef)
    final_10_pvalue.append(p)


plt.bar( np.linspace(0,10,num=10),final_10_pvalue )
plt.savefig("squeez_test_10_pvalue.png")
plt.clf()
plt.cla()
plt.close()
print(final_10_pvalue)
stat, p = sc.kstest(final_10_pvalue,'uniform')
print('final P:',p)

