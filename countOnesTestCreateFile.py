from trng import TrueRandomNumberGenerator
from random import randrange
from tqdm import tqdm,trange
video_source='videotrip.mkv'

words_file=open("slowaZGeneratora.txt",'wt')

T = TrueRandomNumberGenerator(video_source)


for n in tqdm(range(25700000)):
    #temp = [randrange(0,255),randrange(0,255),randrange(0,255),randrange(0,255),randrange(0,255)]#T.rand(5)
    temp = T.rand(5).astype(int)
    word=''
    for j in range(5):
        count = 0
        
        mask = 0b00000001
        for i in range(8):
            if( temp[j] & mask ):
                count+=1
            mask=mask<<1
        
        resault = {
            0 :  'A',
            1 :  'A',
            2 :  'A',
            3 :  'B',
            4 :  'C',
            5 :  'D',
            6 :  'E',
            7 :  'E',
            8 :  'E'
                }[count]
        words_file.write(resault+'\n')
        word+=resault
        #print(temp[j].astype(int),"->",format(temp[j].astype(int),'b'),"->",word,count)
    #print(wordsCounter.keys())

words_file.close()








