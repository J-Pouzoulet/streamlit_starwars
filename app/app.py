import streamlit as st
import pandas as pd
import numpy as np
import requests as rq
import json
from my_funct import get_data, get_data_film, create_file, display_info

st.image('https://www.pixelstalk.net/wp-content/uploads/images6/4K-Star-Wars-HD-Wallpaper-Free-download-768x432.jpg')

st.title(f'Hello *Geeks!!!* :sunglasses:')


res_name = ['None Selected']

col1, col2 = st.columns(2)

with col1:

    option = st.radio(
        'Let\'s geeked! Which StarWars ressouces would you like to access?',
        ('films', 'people', 'planets', 'species', 'starships', 'vehicules'))

with col2:
    text_input = st.text_input(
        f"Search about StarWars {option} here 👇", '')

if text_input == '':
    pass
else: 
    res_name = create_file(option, text_input, res_name)
    res_name = tuple(res_name)
    
    selection = st.selectbox(
        'May the 4th be with you!',
        res_name)

    if selection != 'None Selected':
        res = rq.get(f'https://swapi.dev/api/{option}/?search={selection}').json()
        for item in res['results'][0].keys():
            obj = res['results'][0][item]
            st.write(f'{item} : {obj}')
            
            
            
#for item in dict_name[name].keys():
 #               obj = dict_name[name][item]
 #               st.write(f'{item} : {obj}')




#if st.button('May the 4th be with you'):
 #   res_name, dict_name = create_file(option, text_input)
  #  res_name = tuple(res_name)    
   # name = st.selectbox(
    #    f'Are you looking for this StarWars {option}',
     #   res_name)

    #while name != '':
     #   for item in dict_name[name].keys():
      #      obj = dict_name[name][item]
       #     st.write(f'{item} : {obj}')
        
        