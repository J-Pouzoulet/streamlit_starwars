import streamlit as st
import pandas as pd
import numpy as np
import requests as rq
import json
from PIL import Image

#image = Image.open('home/jerome/code/J-Pouzoulet/IA3/my_first_streamlit/data/wallpaper.jpg')
#image = Image('../data/wallpaper.jpg')
#st.image(image)

st.image('../data/wallpaper.jpg')

st.title(f'Hello *Geeks!!!* :sunglasses:')

#input = ('r2')

#req = rq.request(f'https://swapi.dev/api/people/?search={''}')

col1, col2 = st.columns(2)

with col1:

    option = st.selectbox(
        'Let\'s geeked! Which StarWars ressouces would you like to access?',
        ('','films', 'people', 'planets', 'species', 'starships', 'vehicules'))

with col2:

    text_input = st.text_input(
        f"Search about StarWars {option} here 👇",''
    )

st.write(option == '', text_input == '')

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


#else:       
    #res = json.loads(rq.get(f'https://swapi.dev/api/{option}/?search={text_input}').text) 
    #st.write(res)

#st.markdown(f"# Akinator : la clé : {st.secrets.api_key}")

#st.image("https://fr.akinator.com/bundles/elokencesite/images/akitudes_670x1096/defi.png", width=200)


#st.markdown("## Description")
 
#st.markdown('Lorem ipsum dolor sit amet consectetur adipisicing elit. Dignissimos sunt quod porro nulla omnis nam non earum debitis consectetur ut recusandae, sed quaerat qui iste? Delectus non minima minus dolorum.')

#st.markdown('<a src="https://docs.streamlit.io/library/api-reference">Doc</a>', unsafe_allow_html = True)

#st.latex(r'''
#    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#    \sum_{k=0}^{n-1} ar^k =
#    a \left(\frac{1-r^{n}}{1-r}\right)
#    ''')


#df = pd.DataFrame({
#    'first column': list(range(1, 11)),
#    'second column': np.arange(10, 101, 10)
#})

#df['thirth column'] = df['first column'] * 2


#x1 = st.slider('x?', 1, 11, 3)
#y1 = st.slider('y?', 1, 11, 3)

#def sum(x, y):
#    return x + y
    
#st.write(f"La somme de {x1} et de {y1} est {sum(x1, y1)}")


#lines_number = st.slider('Lines number?', 1, 11, 3)

#head_df = df.head(lines_number)

#head_df

#st.line_chart(df)