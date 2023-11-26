from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service as ChromeService

options = webdriver.ChromeOptions()

service = ChromeService(executable_path="C:\dchrome\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Inicializar el controlador de Chrome
driver = webdriver.Chrome()

#Maximizar Automatizacion
driver.maximize_window()

# Abrir la página web
driver.get("http://opencart.abstracta.us/")
time.sleep(4)

# Ingresar "iPhone" en la barra de búsqueda y hacer clic en el botón de búsqueda
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("iPhone")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# Hacer clic en el primer resultado (iPhone)
first_result = driver.find_element(By.PARTIAL_LINK_TEXT, "iPhone")
first_result.click()
time.sleep(3)

# Hacer clic en el botón "Add to Cart"
add_to_cart_button = driver.find_element(By.ID, "button-cart")
add_to_cart_button.click()
time.sleep(3)

# Hacer clic en el icono del carrito de compras
cart_icon = driver.find_element(By.ID, "cart")
cart_icon.click()
time.sleep(3)

# Hacer clic en el botón "View Cart"
view_cart_button = driver.find_element(By.PARTIAL_LINK_TEXT, "View Cart")
view_cart_button.click()
time.sleep(3)

# Validar que el iPhone esté en el carrito de compras
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "iPhone")))
    print("El iPhone se encuentra en el carrito de compras.")
except:
    print("El iPhone no se encuentra en el carrito de compras.")
time.sleep(3)

# Hacer clic en el botón "Remove" para eliminar el iPhone del carrito de compras
remove_button = driver.find_element(By.XPATH, "//button[@data-original-title='Remove']")
remove_button.click()
time.sleep(3)

# Validar que el iPhone ya no esté en el carrito de compras
try:
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.PARTIAL_LINK_TEXT, "iPhone")))
    print("El iPhone se ha eliminado del carrito de compras.")
except:
    print("El iPhone todavía está en el carrito de compras o ha habido un problema al eliminarlo.")
time.sleep(5)

# Cerrar el navegador
driver.quit()
