from trng import TrueRandomNumberGenerator
from scipy.stats import entropy
import matplotlib.pyplot as plt
import time

#video_source='video2.m4v'
video_source='video12.mp4'

T = TrueRandomNumberGenerator(video_source)

print(T.rand( 100000 ))
print(T.rand( 100 ))
print(T.rand( 100 ))
print(T.rand( 100 ))

plt.hist(T.getSourceVideoSamples(),bins=255,range=[0,255],density=True)
plt.savefig("source.png")
plt.clf()
plt.cla()
plt.close()

plt.hist(T.getAllRandomizedSamples(),bins=256,range=[0,255],density=True)
plt.savefig("resault.png")
plt.clf()
plt.cla()
plt.close()

