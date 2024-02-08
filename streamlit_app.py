import streamlit as st 
import pandas as pd 
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt 
st.title('IRIS FLOWER DASHBOARD')
st.divider()
with st.sidebar:
         c=st.container()
         c.header('DESCRIPTION')
         st.divider()
         c.write('The Iris flower data set or Fishers Iris data set is a multivariate data set used and made famous by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.')
my_dataset = "Iris.csv"
df = pd.read_csv(my_dataset)
if st.checkbox("Preview DataFrame"):
	
	if st.button("Head"):
		st.write(df.head())
	if st.button("Tail"):
		st.write(df.tail())
	else:
		st.write(df.head(2))

# Show Entire Dataframe
if st.checkbox("Show All DataFrame"):
	st.dataframe(df)

# Show Description
if st.checkbox("Show All Column Name"):
	st.text("Columns:")
	st.write(df.columns)
st.divider()



col1 ,col2 = st.columns(2)
	


        
        
        
        
        

    
    
    











