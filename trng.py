import numpy as np
import cv2

class TrueRandomNumberGenerator:

    def __init__(self, video_source):
        self.video_source = str(video_source)

        #cap = cv2.VideoCapture(0) # Pobierz dane z kamerki
        self.cap = cv2.VideoCapture(self.video_source) # Pobierz dane z nagrania
        print("CV2 open = ", self.cap.isOpened())
        self.bits = 8
        self.mask = 0b00000011
        self.NumSoFar = 0
        self.Frame=self.__getFrames(1)[0]
        self.Frames=np.array([self.Frame])
        self.FinalList = np.array([])
        self.x,self.y=(0,0)
        self.Randomized=0

        self.FinalByteArray = bytearray([])

    
    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def __reset(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.cap = cv2.VideoCapture(self.video_source)

    def __resetList(self):
        self.FinalList = np.array([])
        self.Randomized = 0



    def getAllRandomizedSamples(self):
        return self.FinalByteArray
        #return self.FinalList

    def getSourceVideoSamples(self):
        #print(self.Frames.ravel().shape)
        return self.Frames.ravel()

    def rand(self,count=100,bits = 8, infoText=False):

        if( self.FinalList.size>3e5+count ):
            self.__resetList()

        self.bits = bits
        self.NumNeeded=count+self.Randomized
        self.NumSoFar=self.FinalList.size
        i=0
        while (self.NumSoFar < self.NumNeeded):
            #Jeżeli dane z ramki się skończyły
            if self.Frame.shape[0]<=self.x+2 or self.Frame.shape[1]<=self.y+4:
                self.Frame=self.__getFrames(1)[0]
                self.x,self.y=(0,0)
                #print(self.Frame)
                np.append(self.Frames,self.Frame)

            self.FinalList = np.concatenate((self.FinalList,self.__takeOne().ravel()),axis=None)
            
            self.NumSoFar = self.FinalList.size
            i+=1     
            if(infoText):
                print(self.NumSoFar)
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
                #if cv2.waitKey(1) & 0xFF == ord('q'):
                #    break
                i+=1
            else:
                self.__reset()
                ret, frame = self.cap.read()
                frames.append(frame)
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
        Sub = np.array([],dtype='uint32')
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
        
        
        for i in range(0,Sub.size-round(self.bits/2),round(self.bits/2)):
            b = Sub[i].astype('uint32')            
            for j in range(2,self.bits,2):
                b = b ^ (Sub[round(i+(j/2))]<<j).astype('uint32')
        
            final.append(b)


        return np.array(final)
    
