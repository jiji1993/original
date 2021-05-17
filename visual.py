#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns 



st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Dataset")


#import dataset
df = pd.read_csv('sample.csv')
#First thirty rows
tips = df.head()
#Display the table
st.table(tips)
st.header("Visualisation Using Seaborn")


#bar plot
st.subheader("Bar Plot")
tips.plot(kind='bar')
st.pyplot()

#Displot
st.subheader("Displot")
sns.displot(tips['Period'])
st.pyplot()


#pairplot
st.subheader("Pairplot")
sns.pairplot(tips,hue='STATUS',palette='rainbow')
st.pyplot()


fig = plt.figure()
fig.patch.set_facecolor('black')

cm = sns.light_palette("green", as_cmap=True)
  

tips.style.set_properties({'background-color': 'black',
                           'color': 'green'})