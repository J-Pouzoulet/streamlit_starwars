import json
import requests as rq
import streamlit as st

def get_data(res, res_name):
    for i in range(len(res['results'])):
        #dict_name[res['results'][i]['name']] = res['results'][i]
        res_name.append(res['results'][i]['name'])
    return res_name

def get_data_film(res, res_name):
    for i in range(len(res['results'])):
        #dict_name[res['results'][i]['title']] = res['results'][i]
        res_name.append(res['results'][i]['title'])
    return res_name


def create_file(option, text_input):
    if option != 'films':
            res = rq.get(f'https://swapi.dev/api/{option}/?search={text_input}').json()
            res_name = ['None Selected']
            #dict_name = {}

            res_name = get_data(res, res_name)

            while res['next'] != None:
                res = rq.get(res['next']).json()
                res_name = get_data(res, res_name)
                        
    else:
        res = rq.get(f'https://swapi.dev/api/{option}/?search={text_input}').json()
        res_name = ['None Selected']
        #dict_name = {}

        res_name = get_data_film(res, res_name)

        while res['next'] != None:
            res = rq.get(res['next']).json()
            res_name = get_data(res, res_name)        
            
    return res_name
        
def display_info(option, name):
    res = rq.get(f'https://swapi.dev/api/{option}/?search={name}').json()
    for item in res['results'][0].keys():
        obj = res['results'][0][item]
        return st.write(f'{item} : {obj}')