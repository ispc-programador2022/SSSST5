import random
from time import sleep
from selenium import webdriver


driver = webdriver.Chrome('./chromedriver.exe')


driver.get('https://www.olx.com.ec/autos_c378')

#if __name__ == '__main__':
#    response = requests.get(website)

#    if response.status_code == 200:
#        content = response.text

#        with open('olx.html', encoding='utf-8', mode='w+') as file:

#            file.write(content)


boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
for i in range(20):
    try:
        boton.click()
        sleep(random.uniform(8.0, 10.0))
        boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
    except:
        break


autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')



for auto in autos:
    precio = auto.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
    print (precio)
    descripcion = auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
    print (descripcion)