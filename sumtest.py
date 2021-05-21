import random
import matplotlib.pyplot as plt
from scipy.stats import normaltest, kstest
from trng import TrueRandomNumberGenerator

T=TrueRandomNumberGenerator("videotrip.mkv")

final_p_values=[]
for fv in range(10):
    p_values=[]
    for pv in range(100):

        list_to_sum = []
        n=200
        for i in range(n):
            #f = random.randrange(0,2**32)/2**32
            f = T.rand(1,bits=32)[0]/2**32
            list_to_sum.append(f)
        sums = []
        for i in range(n-100):
            sums.append( sum( list_to_sum[i:i+100] ) )
        n,bins,patches=plt.hist(sums, density=True)
        stats, p = kstest(n, 'norm')
        #stats, p = normaltest(n)
        print(stats, p)

        p_values.append(p)
        
        #plt.savefig("sums.png")
        plt.clf()
        plt.cla()
        plt.close()

        #print(sums)
        
    #print(p_values)
    #n,bins,patches=plt.hist(p_values)
    #plt.savefig("P-values_sums_random.png")
    plt.clf()
    plt.cla()
    plt.close()

    stats, p = kstest(p_values,'norm')
    final_p_values.append(p)



print(final_p_values)
n,bins,patches=plt.hist(final_p_values)
plt.savefig("P-values_sums_final_random.png")
plt.clf()
plt.cla()
plt.close()

stats, p = kstest(final_p_values,'norm')
print('final p:',p)

