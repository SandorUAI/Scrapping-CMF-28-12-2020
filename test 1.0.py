#Librerias necesarias
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import  ActionChains
import pandas as pd

#Funciones necesarias

def encontrar_mes_incio():
	#Abrir calendario de inicio
	calendario_1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[4]/form/div[1]/img")))
	calendario_1.click()

	##Abrir selector de mes de inicio
	mes_1_selector = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/select[1]")))
	mes_1_selector.click()

	##Selecionar mes de inicio
	mes_1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/select[1]/option[1]")))
	mes_1.click()

	##Abrir selector de año de inicio
	año_1_selector = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/select[2]")))
	año_1_selector.click()

	##Selecionar año de inicio
	año_1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/select[2]/option[1]")))
	año_1.click()

	##Seleccionar día de inicio
	dia_1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/table/tbody/tr[1]/td[1]/a")))
	dia_1.click()

def encontrar_mes_termino():
	#Abrir calendario de cierre
	calendario_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[4]/form/div[2]/img")))
	calendario_2.click()

	##Abrir selector de mes de cierre
	mes_2_selector = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/select[1]")))
	mes_2_selector.click()

	##Selecionar mes de cierre
	mes_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/select[1]/option[12]")))
	mes_2.click()

	##Abrir selector de año de cierre
	año_2_selector = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/select[2]")))
	año_2_selector.click()

	##Selecionar año de cierre
	año_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/select[2]/option[20]")))
	año_2.click()

	##Seleccionar día de cierre
	dia_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/table/tbody/tr[1]/td[5]/a")))
	dia_2.click()

def click_consultar_fecha():
	consultar_boton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[4]/form/div[3]/input")))
	consultar_boton.click()

def extraer_cargos():
    for row in Table_empresa_loops:
        try:
            if('Director' in row and 'Suplente' in row):
                Cargos_por_empresa.append('Director_suplente')
            else:
                for b in row:
                    if (b == 'Presidente'):
                        Cargos_por_empresa.append(b)
                    elif (b == 'Vicepresidente'):
                        Cargos_por_empresa.append(b)
                    elif (b == 'Director'):
                        Cargos_por_empresa.append(b)
        except:
            continue

def extraer_fecha_nombramiento():
    rango = len(Table_empresa_loops) + 3
    for a in range(rango):
	    if a < 3:
	        pass
	    else:
	        xpath_fecha_nombramientos = [f"/html/body/div[1]/div[4]/div[4]/table[2]/tbody/tr[{a}]/td[4]"]
	        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_fecha_nombramientos[0])))
	        Fecha_inicial_por_empresa.append(driver.find_element_by_xpath(xpath_fecha_nombramientos[0]).text)

def extraer_fecha_termino():
    rango = len(Table_empresa_loops) + 3
    for a in range(rango):
	    if a < 3:
	        pass
	    else:
	        extraer_fecha_termino = [f"/html/body/div[1]/div[4]/div[4]/table[2]/tbody/tr[{a}]/td[5]"]
	        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, extraer_fecha_termino[0])))
	        Fecha_final_por_empresa.append(driver.find_element_by_xpath(extraer_fecha_termino[0]).text)

def extraer_nombres_personas():
    rango = len(Table_empresa_loops) + 3
    for a in range(rango):
	    if a < 3:
	        pass
	    else:
	        extraer_nombre_persona = [f"/html/body/div[1]/div[4]/div[4]/table[2]/tbody/tr[{a}]/td[2]"]
	        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, extraer_nombre_persona[0])))
	        Nombres_por_persona.append(driver.find_element_by_xpath(extraer_nombre_persona[0]).text)

def extraer_rut_empresas():
	for i in range(926):
		if (i/2).is_integer() == False:
			Empresas_rut.append(Table_pagina_principal[i])

def extraer_nombre_empresas():
	for i in range(926):
		if (i/2).is_integer() == False:
			empresas_rut.append(Table_pagina_principal[i])

# DRIVER
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://www.cmfchile.cl/institucional/mercados/listado_actual_directorios.php?mercado=V")


#Variables necesarias
Nombres_por_persona = []

empresas_nombre = []

Cargos_por_empresa = []

Fecha_final_por_empresa = []

Fecha_inicial_por_empresa = []

Empresas_rut = []


#Listas necesarias
Table_pagina_principal = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[4]/table").text.split("\n")
extraer_rut_empresas()

## loop final
for i in range(466):
	try:
		if i < 1:
			pass
		else:
			Xpath_pagina_empresa = [f"/html/body/div[1]/div[4]/div[4]/table/tbody/tr[{i}]/td[1]/a"]
			Link_pagina_empresa = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Xpath_pagina_empresa[0])))
			Link_pagina_empresa.click()
			encontrar_mes_incio()
			encontrar_mes_termino()
			click_consultar_fecha()
			Table_empresa = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[4]/table[2]")))
			Table_empresa = Table_empresa.text.split("\n")
			Table_empresa.pop(0)
			Table_empresa.pop(0)
			Table_empresa_loops = [a.split(" ") for a in Table_empresa]
			Ruts_personas = [i[0] for i in Table_empresa_loops]
			extraer_cargos()
			extraer_fecha_nombramiento()
			extraer_fecha_termino()
			extraer_nombres_personas()
			Data = [Ruts_personas, Nombres_por_persona, Cargos_por_empresa, Fecha_inicial_por_empresa, Fecha_final_por_empresa]
			df = pd.DataFrame(Data)
			df = df.transpose()
			df.columns = ['Rut_individuo', 'Nombre', 'Cargo', 'Fecha_nombramiento', 'Fecha_termino']
			nombre_archivo =  [f"{Empresas_rut[i-1]}.csv"]
			df.to_csv(nombre_archivo[0])
			Ruts_personas.clear()
			Nombres_por_persona.clear()
			Cargos_por_empresa.clear()
			Fecha_inicial_por_empresa.clear()
			Fecha_final_por_empresa.clear()
			driver.implicitly_wait(1)
			driver.back()
			driver.back()
	except:
		print(f"{i} ERROR!!!")
		continue



