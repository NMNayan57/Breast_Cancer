# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 20:26:16 2022

@author: USER
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading saves model



Breast_model=pickle.load(open('C:/Users/USER/Desktop/Multiple disease prediction system/saved models/Breast_model.sav','rb'))






#side bar for navigations

with st.sidebar:
    selected=option_menu(
                        '
                           'Breast cancer prediction',
                           '],
                          
                          icons=[''wind'],
                          
                            default_index=0)
    
  
    
    
    
    
    #Breast cancer prediction page
if(selected=='Breast cancer prediction'):

    #page title
    st.title('Breast cancer prediction using machine learnig')
    
    
    #getting the input data from user
    #colum for input fields
    
    col1,col2,col3= st.columns(3)
    
    with col1:
       mean_radius = st.text_input('mean_radius')
        
    with col2:
       mean_texture = st.text_input('mean_texture')
        
    with col3:
        mean_perimeter = st.text_input('mean_perimeter value')
        
        
    with col1:
       mean_area = st.text_input('mean_area')
    
    with col2:
     mean_smoothness = st.text_input('mean_smoothness')
        
    
        
        
    
    
    #code for prediction
    
    Breast_diagnosis= ''
    
    #creating button for predictions
    
    if st.button('Breast cancer Test Results'):
        Breast_prediction= Breast_model.predict([[ mean_radius,mean_texture ,  mean_perimeter, mean_area,mean_smoothness]])
        if( Breast_prediction[0]==0):
            Breast_diagnosis=' The person do not have breast cancer'
        else:
            Breast_diagnosis='The person has breast cancer'
            
    st.success(Breast_diagnosis)  






    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

     
     
            
            