from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from pandas import *
from flask import Flask, render_template

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

#------------------titulo de la noticia------------------------
def scrape():
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    articles = soup.find_all('div', class_='image_and_description_container')
    for article in articles:
        try:
            titulo1 = article.find('div', class_='bottom_gradient')
            news_title = titulo1.find('h3').text
            #print(news_title)
            break
            
        except:
            print("Sin Título")
    #return news_title
#------------------contenido de la noticia------------------------    
#def noticia_contenido():
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    articles = soup.find_all('div', class_='image_and_description_container')
    for article in articles:
        try:
            news_p = article.find('div', class_='rollover_description_inner').text
            #print(news_p)
            break
        except:
            print("Sin Título")
    #return news_p
#-----------------url de la imagen-----------------------------
#def imagen():
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('div', class_='image_and_description_container')
    for image in images:
        try:
            imagen = image.find('img', class_='thumb')
            href = imagen['src']
            href_completa = 'https://www.jpl.nasa.gov' + href
            break
        except:
            print("Scraping Complete")
    #return href_completa
#-----------------------Twitter---------------------------
#def twitter():
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find_all('div', class_='js-tweet-text-container')
    for article in articles:
        titulo1 = article.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
        break
    try:
        browser.click_link_by_partial_text('next')
    except:
        print("Scraping Complete")

#------------------------Mars Facts--------------------------------
    url = 'https://space-facts.com/mars/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    articles = soup.find_all('table', class_='tablepress tablepress-id-mars')

    for article in articles:
        try:
            row1= article.find('tr', class_='row-1 odd')
            columna1_1 = row1.find('td', class_='column-1').text
            columna2_1 = row1.find('td', class_='column-2').text
            print('----------------')
            print(columna1_1)
            print(columna2_1)

            row2= article.find('tr', class_='row-2 even')
            columna1_2 = row2.find('td', class_='column-1').text
            columna2_2 = row2.find('td', class_='column-2').text
            print('----------------')
            print(columna1_2)
            print(columna2_2)
    
            row3= article.find('tr', class_='row-3 odd')
            columna1_3 = row3.find('td', class_='column-1').text
            columna2_3 = row3.find('td', class_='column-2').text
            print('----------------')
            print(columna1_3)
            print(columna2_3)
    
            row4= article.find('tr', class_='row-4 even')
            columna1_4 = row4.find('td', class_='column-1').text
            columna2_4 = row4.find('td', class_='column-2').text
            print('----------------')
            print(columna1_4)
            print(columna2_4)
    
            row5= article.find('tr', class_='row-5 odd')
            columna1_5 = row5.find('td', class_='column-1').text
            columna2_5 = row5.find('td', class_='column-2').text
            print('----------------')
            print(columna1_5)
            print(columna2_5)
    
            row6= article.find('tr', class_='row-6 even')
            columna1_6 = row6.find('td', class_='column-1').text
            columna2_6 = row6.find('td', class_='column-2').text
            print('----------------')
            print(columna1_6)
            print(columna2_6)
    
            row7= article.find('tr', class_='row-7 odd')
            columna1_7 = row7.find('td', class_='column-1').text
            columna2_7 = row7.find('td', class_='column-2').text
            print('----------------')
            print(columna1_7)
            print(columna2_7)
    
            row8= article.find('tr', class_='row-8 even')
            columna1_8 = row8.find('td', class_='column-1').text
            columna2_8 = row8.find('td', class_='column-2').text
            print('----------------')
            print(columna1_8)
            print(columna2_8)
    
            row9= article.find('tr', class_='row-9 odd')
            columna1_9 = row9.find('td', class_='column-1').text
            columna2_9 = row9.find('td', class_='column-2').text
            print('----------------')
            print(columna1_9)
            print(columna2_9)
            break
        except:
            print("Scraping Complete")

        # initialize list of lists 
    data = [[columna1_1, columna2_1], 
        [columna1_2, columna2_2], 
        [columna1_3, columna2_3], 
        [columna1_4, columna2_4], 
        [columna1_5, columna2_5], 
        [columna1_6, columna2_6], 
        [columna1_7, columna2_7], 
        [columna1_8, columna2_8], 
        [columna1_9, columna2_9], 
        [columna1_2, columna2_2]]

    # Create the pandas DataFrame 
    df = pd.DataFrame(data, columns = ['Concept', 'Measure']) 
    result_html = df.to_html()  

#------------------------------Imágenes de hemisferios---------------------------

    hemisphere_image_urls = [{"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
                            {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
                            {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
                            {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"}]



    diccionario_completo = [{"Noticia": news_title, "Contenido": news_p, "Imagen": href_completa, "Clima en Marte": titulo1, 
                            "Mars Facts": result_html,"Imagenes de hemisferios": hemisphere_image_urls}]

    return diccionario_completo
