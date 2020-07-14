from selenium import webdriver
import time


def typings(mon1, mon2):
    # creates a new browser in order to get the typings of each mon selected
    driver = webdriver.Chrome()

    driver.get('https://play.pokemonshowdown.com/')
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_xpath('//button[@class="button mainmenu2"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//button[@name="newTop"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//button[@class="select formatselect teambuilderformatselect"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//button[@value="gen8nationaldex"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//button[@name="addPokemon"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//input[@type="text"]').send_keys(mon1)
    types1 = driver.find_elements_by_xpath('//img[@alt]')
    typeStr1 = []
    for x in types1:
        typeStr1.append(x.get_attribute('alt'))

    driver.find_element_by_xpath('//input[@type="text"]').clear()
    driver.find_element_by_xpath('//input[@type="text"]').send_keys(mon2)
    types2 = driver.find_elements_by_xpath('//img[@alt]')
    typeStr2 = []
    for y in types2:
        typeStr2.append(y.get_attribute('alt'))

    types = [typeStr1, typeStr2]
    driver.close()
    return types
