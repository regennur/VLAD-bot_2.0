import requests
from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup

def getRif(word="кот"):
    res_t = show_word(word)
    if 'data' in res_t:
        res = res_t['data']

    return res

def show_word(word):
    response = requests.get('https://rifmu.ru/' + word)
    contents_html = response.content

    soup = BeautifulSoup(contents_html, 'lxml')
    text_arr = []
    if soup.ul == None: 
        return  {"data": []}
    for child in soup.ul.recursiveChildGenerator():

        if child.name == 'a':

            text_arr.append(child.text)

    return {"data": text_arr}
