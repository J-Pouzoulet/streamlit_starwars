import streamlit as st
import pandas as pd
import numpy as np
import requests as rq
import json

st.image('https://www.pixelstalk.net/wp-content/uploads/images6/4K-Star-Wars-HD-Wallpaper-Free-download-768x432.jpg')

st.title(f'Hello *Geeks!!!* :sunglasses:')

col1, col2 = st.columns(2)

with col1:

    option = st.selectbox(
        'Let\'s geeked! Which StarWars ressouces would you like to access?',
        ('','films', 'people', 'planets', 'species', 'starships', 'vehicules'))

with col2:

    text_input = st.text_input(
        f"Search about StarWars {option} here 👇",''
    )

if option == '' or text_input == '':
    pass
else:
    if option != 'films':
        res = json.loads(rq.get(f'https://swapi.dev/api/{option}/?search={text_input}').text)
        res_name = ['']
        dict_name = {}
        count = 0
        for i in range(res['count']):
            dict_name[res['results'][i]['name']] = count
            res_name.append(res['results'][i]['name'])
            count += 1
        res_name = tuple(res_name)    
        name = st.selectbox(
                f'Are you looking for this StarWars {option}',
                res_name)
        if name == '':
            pass
        else:
            for item in res['results'][dict_name[name]].keys():
                obj = res['results'][dict_name[name]][item]
                st.write(f'{item} : {obj}')
    else:
        res = json.loads(rq.get(f'https://swapi.dev/api/{option}/?search={text_input}').text)
        res_title = ['']
        dict_title = {}
        count = 0
        for i in range(res['count']):
            dict_title[res['results'][i]['title']] = count
            res_title.append(res['results'][i]['title'])
            count += 1
        res_title = tuple(res_title)    
        title = st.selectbox(
                f'Are you looking for this StarWars {option}',
                res_title)
        if title == '':
            pass
        else:
            for item in res['results'][dict_title[title]].keys():
                obj = res['results'][dict_title[title]][item]
                st.write(f'{item} : {obj}')