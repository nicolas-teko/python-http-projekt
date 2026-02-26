# myproject.py
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By


def handle_get(parameter=None):
    url = "https://google.com"
    driver = webdriver.Edge()
    driver.get(url)

    # Wenn nur "get" ohne Parameter
    if parameter is None:
        print("Seite wurde geöffnet.")
        input("Drücke Enter zum Beenden...")
        driver.quit()
        return

    parameter = parameter.lower()

    try:
        if parameter == "title":
            print("Title:", driver.title)

        elif parameter == "h1":
            element = driver.find_element(By.TAG_NAME, "h1")
            print("H1:", element.text)

        elif parameter == "img":
            images = driver.find_elements(By.TAG_NAME, "img")
            if not images:
                print("Keine Bilder gefunden.")
            for img in images:
                print("Image src:", img.get_attribute("src"))

        else:
            print("Unbekannter Parameter.")

    except Exception as e:
        print("Fehler:", e)

    input("Drücke Enter zum Beenden...")
    driver.quit()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Bitte Befehl angeben (z.B. get)")
    else:
        command = sys.argv[1].lower()

        if command == "get":
            if len(sys.argv) == 3:
                handle_get(sys.argv[2])
            else:
                handle_get()
        else:
            print("Befehl nicht unterstützt.")