import numpy as np
import math
import scipy.stats as sc
import matplotlib.pyplot as plt
import random
from numpy import random as ran
from trng import TrueRandomNumberGenerator

def DIE(T):
    UNIMAX = pow(2,8)
    DIE = (1+int(6*(T.rand(1)/UNIMAX)))
    #DIE = ran.randint(1,7) #test external generator
    return DIE

def insertThrows(throws,Of):
    if throws>20: Of[20]+=1
    else: Of[throws]+=1
    return Of

def crapstest(T,N):

    no_games = N
    no_wins = 0
    i = 0
    Of = np.zeros(21)
    Ef = np.zeros(21)
    sum = 0
    
    print("\n\nCRAPTEST IN PROGRESS...\n")
    
    #compute the expected frequencies
    sum=1/3.
    Ef[0] = 1/3.
    for i in range(1,20):
        Ef[i] = (27*pow(27/36.,i-1)+40*pow(26/36.,i-1)+55*pow(25/36.,i-1))/648
        sum+=Ef[i]
        
    Ef[20] = 1.-sum
    
    Ef*=no_games
    
    print("Ef:")
    print(Ef)
    
    #playing the games
    while i < no_games:
        no_throws = 0
        
        throw_first=DIE(T)+DIE(T)
        
        if throw_first in (7,11): 
            no_wins+=1
            Of = insertThrows(no_throws,Of)
            i+=1
            continue
            
        if throw_first in (2,3,12): 
            Of = insertThrows(no_throws,Of)
            i+=1
            continue
        
        while 1==1:
            throw_next=DIE(T)+DIE(T)
            no_throws+=1
            
            if throw_next == 7: 
                no_wins+=1
                break
                
            if throw_next == throw_first:
                break
        i+=1
        
        Of = insertThrows(no_throws,Of)
        
    
    mean=244*no_games/495.
    std=math.sqrt(mean*251/495.)
    t=(no_wins-mean)/std
    
    print("Of:")
    print(Of)
    
    #plt.hist(Of,bins=20,range=[1,21],density=False)
    plt.plot(Of)
    plt.savefig("crapshist.png")
    plt.clf()
    plt.cla()
    plt.close()
   
    print("\n\t\t\tGAME RESULTS:");
    print("\tNo. of wins:  Observed\tExpected");
    print("\t                ",no_wins,"\t",mean);
    print("\t_____________________________________________________________\n\n");
    
    chi2,pvalue_th=sc.chisquare(f_obs=Of,f_exp=Ef)
    
    print("\t\t\tSUMMARY of craptest:");
    print("\t p-value for throws/game: ",pvalue_th);
    print("\t_____________________________________________________________\n\n");
    
    
video_source='video1.mp4'

T = TrueRandomNumberGenerator(video_source)

crapstest(T,15000)
