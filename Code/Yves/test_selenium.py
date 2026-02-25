from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Webseite öffnen
driver = webdriver.Edge()
driver.get('https://www.youtube.com')
sleep(3)


# POST für suche starten
search_bar = driver.find_element(By.NAME, 'search_query')
search_bar.send_keys('Selenium Tutorial')
# POST für Button Search klick
button_click = driver.find_element(By.CLASS_NAME, 'ytSearchboxComponentSearchButton')
button_click.click()
sleep(3)

# Titel vom Header anzeigen
titel_seite = driver.title
print(f"Seitentitel: {titel_seite}")


input("Drücke Enter zum Beenden...")
driver.quit()