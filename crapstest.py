import numpy as np
import math
import scipy.stats as sc
from trng import TrueRandomNumberGenerator



def getRandomInRange(T,a,b):
    value = T.rand(1,bits=4)
    while value<a or value>b:
        value = T.rand(1,bits=4)
    return value

def crapstest(T,N):

    no_games = N
    no_wins = 0
    i = 0
    throws = np.empty(0)
    
    print("\n\nTEST IN PROGRESS...\n")
    
    while i < no_games:
        no_throws = 0
        
        throw_first=getRandomInRange(T,1,6)+getRandomInRange(T,1,6)
       
        if throw_first in (7,11): 
            no_wins+=1
            throws = np.append(throws,[no_throws])
            i+=1
            continue
            
        if throw_first in (2,3,12): 
            throws = np.append(throws,[no_throws])
            i+=1
            continue
        
        while 1==1:
            throw_next=getRandomInRange(T,1,6)+getRandomInRange(T,1,6)
            no_throws+=1
            
            if throw_next == 7: 
                no_wins+=1
                break
                
            if throw_next == throw_first:
                break
        i+=1
        throws = np.append(throws,[no_throws])
    
        
    
    mean=244*no_games/495.
    std=math.sqrt(mean*251/495.)
    t=(no_wins-mean)/std
    pvalue_w=1-sc.chi2.pdf(t,20)
   
    print("\t\t\tGAME RESULTS:");
    print("\tNo. of wins:  Observed\tExpected");
    print("\t                ",no_wins,"\t",mean);
    print("\t_____________________________________________________________\n\n");
    print("\tz-score=",t," pvalue=",pvalue_w);
    print("\n\t_____________________________________________________________\n\n");
    
    x,p=sc.chisquare(throws,ddof=20);
    pvalue_th=1-p
    
    print("\t\t\tSUMMARY of craptest:");
    print("\t p-value for no. of wins: ",pvalue_w);
    print("\t p-value for throws/game: ",pvalue_th);
    print("\t_____________________________________________________________\n\n");
    

video_source='video1.mp4'

T = TrueRandomNumberGenerator(video_source)

crapstest(T,15000)


