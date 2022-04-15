from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pesquisa = input("Digite a pesquisa:")

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")

driver = webdriver.Chrome(r'P:\Programação\python\chromedriver', options=options)
driver.get("https://www.google.com")
#Abriu o google

campo = driver.find_element_by_xpath("//input[@aria-label='Pesquisar']")
campo.send_keys(pesquisa)
campo.send_keys(Keys.ENTER)
#Clicar no buscar, incluir a pesquisa digitada pelo usuário enter
resultados = driver.find_element_by_xpath("//*[@id='result-stats']").text
print(resultados)
#Mostrar a quantidade de resultados encontrados

numero_resultados = int(resultados.split("Aproximadamente ")[1]
                                    .split(" resultados")[0].replace('.', ''))
maximo_paginas = numero_resultados/10

print(f"Número de páginas: {maximo_paginas}")
#Para fomatar o numero de resultados para números de páginas fazemos acima

