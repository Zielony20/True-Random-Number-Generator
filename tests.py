from trng import TrueRandomNumberGenerator
from scipy.stats import entropy
import matplotlib.pyplot as plt
import time
import numpy as np

def MyEntropy(n):
    result = 0
    for i in n:
        result+= i* np.log2(1/i)
    return result

video_source='video6.mp4'

start = time.time()
T = TrueRandomNumberGenerator(video_source)
print(T.rand( 200000 ))
end = time.time()

n, bins, patches = plt.hist(T.getSourceVideoSamples(),bins=255,range=[0,255],density=True)
plt.savefig("source.png")
plt.clf()
plt.cla()
plt.close()

print("Entropy of raw data:",entropy(n,base=2))

n, bins, patches = plt.hist(T.getAllRandomizedSamples(),bins=255,range=[0,255],density=True)
plt.savefig("resault.png")
plt.clf()
plt.cla()
plt.close()

print("Entropy after postprocessing:",entropy(n,base=2))
print("time:",end - start)