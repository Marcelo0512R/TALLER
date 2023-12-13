import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

def cambiar_caracter(texto):
    return texto.replace('Ñ', 'N')

driver = webdriver.Chrome()
driver.get('https://datosmacro.expansion.com/pib/ecuador')
html_pagina = driver.page_source
contenido = BeautifulSoup(html_pagina, 'html.parser')

datos = contenido.find('table')
fecha = []
euros = []
dolares = []
porcentaje = []

if datos:
    filas_tabla = datos.find_all('tr')
    for fila in filas_tabla[1:]:
        celdas = fila.find_all('td')
        fecha.append(cambiar_caracter(celdas[0].text.strip()))
        euros.append(cambiar_caracter(celdas[1].text.strip()))
        dolares.append(cambiar_caracter(celdas[2].text.strip()))
        porcentaje.append(cambiar_caracter(celdas[3].text.strip()))

dataframe_pib = pd.DataFrame({
    '<FECHA>': fecha,
    'PIB ANUAL Euros ': euros,
    'PIB ANUAL Dólares ': dolares,
    'Var PIB.': porcentaje
})

dataframe_pib.to_csv('datosEcuador.csv', index=False, encoding='utf-8-sig')

# VERA RENDON ANGIE
#HERRERA GUIJARRO ODALIS
#IDROVO UBE LEONELA
#REINOSO INDACOCHEA LUIS