from trng import TrueRandomNumberGenerator
from scipy.stats import entropy
import matplotlib.pyplot as plt
import streamlit as st
import io
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

video_source = st.file_uploader("upload video source", type='mp4')

def MyEntropy(n):
    result = 0
    for i in n:
        result+= i* np.log2(1/i)
    return result


if video_source:

    g = io.BytesIO(video_source.read())  ## BytesIO Object
    temporary_location = "testout_simple.mp4"

    with open(temporary_location, 'wb') as out:  ## Open temporary file as bytes
        out.write(g.read())  ## Read bytes into file

    # close file
    out.close()

    if st.button('generate samples'):
        T = TrueRandomNumberGenerator(temporary_location)

        temp=T.rand( 100000 ,bits=8 )

        
        hist_data = temp
        df = pd.DataFrame({"samples": hist_data})
        print(df)
        fig = px.histogram(df,x="samples", facet_col_spacing=1,
                           marginal="violin", histnorm=None, barmode="overlay")
        st.plotly_chart(fig, use_container_width=True)

        n, _,_ = plt.hist(temp,bins=256,range=[0,255],density=True)
        st.text("Entropy of raw data: {}".format(entropy(n, base=2)))
        #st.text("Entropy of raw data: {}".format(MyEntropy(temp)))



#start = time.time()
