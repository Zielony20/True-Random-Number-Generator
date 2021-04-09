import numpy as np
import cv2

class TrueRandomNumberGenerator:

    def __init__(self, video_source,):
        self.video_source = video_source

        #cap = cv2.VideoCapture(0) # Pobierz dane z kamerki
        self.cap = cv2.VideoCapture(self.video_source) # Pobierz dane z nagrania
        print("CV2 open = ", self.cap.isOpened())

        self.mask = 0b00000011
        self.NumSoFar = 0
        self.Frame=self.__getFrames(1)[0]
        self.Frames=np.array([self.Frame])
        self.FinalList = np.array([])
        self.x,self.y=(0,0)
        self.Randomized=0
    
    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()
    
    def getAllRandomizedSamples(self):
        return self.FinalList

    def getSourceVideoSamples(self):
        #print(self.Frames.ravel().shape)
        return self.Frames.ravel()

    def rand(self,count=100 ):
        self.NumNeeded=count+self.Randomized
        self.NumSoFar=self.FinalList.size
        i=0
        while (self.NumSoFar < self.NumNeeded):
            #Jeżeli dane z ramki się skończyły
            if self.Frame.shape[0]<=self.x+2 or self.Frame.shape[1]<=self.y+4:
                self.Frame=self.__getFrames(1)[0]
                self.x,self.y=(0,0)
                np.append(self.Frames,self.Frame)

            self.FinalList = np.concatenate((self.FinalList,self.__takeOne().ravel()),axis=None)
            self.NumSoFar = self.FinalList.size
            i+=1     
            #print(self.NumSoFar)
        self.Randomized+=count
        return self.FinalList[self.Randomized-count:self.Randomized]

    #pobranie obrazów ze źródła
    #zwraca tablicę 4 wymiarową
    #Wymiarami są: numer klatki, numer wiersza, numer kolumny, numer koloru RGB
    def __getFrames(self,countOfFrames=1):
        frames=[]
        i=0
        while(i<countOfFrames):
            ret, frame = self.cap.read()
            if(ret):
                #cv2.imshow('Image', frame)
                frames.append(frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                i+=1
        #print(len(frames[0]))
        return np.array(frames)
        
    #funkcja obcina wskazane wartości graniczne
    def __pickOut(self,SubList,min_,max_):
        SubList = SubList[SubList<max_]
        SubList = SubList[SubList>min_]
        return SubList

    #pobierz z klatki dane ze wskazanych współrzędnych
    #zwraca współrzędne na których skończył pobieranie
    def __takeOne(self):
        final = []
        Sub = np.array([],dtype='uint8')
        for i in range(20):
            a =  self.Frame[self.x:self.x+2,self.y:self.y+3,:]
            self.x += 3
            self.y += 4
            if(i%2==0):    
                a=np.rot90(a,k=1,axes=(0,1)) # obróć
            a = self.__pickOut(a,5,250)
            a = self.mask&a
            a=a.ravel()
            Sub = np.concatenate((Sub,a),axis=None)
        z = np.floor( np.sqrt( Sub.shape[0] )).astype(int)
        
        Sub=np.reshape(Sub[0:(z*z).astype(int)],(z,z))    
        Sub = np.flip(Sub.T) # Obróc
        Sub = Sub.ravel()
        for i in range(0,Sub.size-4,4):
            b = (Sub[i]   ^
            (Sub[i+1]<<2) ^ 
            (Sub[i+2]<<4) ^  
            (Sub[i+3]<<6)).astype('uint8')
            final.append(b)
        return np.array(final)
    
