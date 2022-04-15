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

url_pagina = driver.find_element_by_xpath("//a[@aria-label='Page 2']").get_attribute("href")
#O href vai mudar sempre, ou seja, ele que vai diferenciar uma página de outra

pagina_atual = 0
start = 10
while pagina_atual <= 10:
    if not pagina_atual == 0:
        url_pagina = url_pagina.replace(f"start={start}", 
                                        f"start={start+10}")
        start = start+10
    pagina_atual = pagina_atual+1
    driver.get(url_pagina)
    #Criar um looping para mudança de página

    divs = driver.find_elements_by_xpath("//div[@class='g']")
    #element = uma só infomação ; elements = mais que uma informação
    for div in divs:
        nome = div.find_element_by_tag_name("h3")
        link = div.find_element_by_tag_name("a")
        resultado = f"{nome.text} ; {link.get_attribute('href')}"
        print(resultado)