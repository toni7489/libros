from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from generar_subdominio import email, nombre_email, nombre_completo
from generar_mensajes import mensaje_estructurado

# Configurar el controlador de Firefox utilizando GeckoDriverManager
service = Service(GeckoDriverManager().install())
options = webdriver.FirefoxOptions()

# Iniciar el navegador con el controlador y las opciones
driver = webdriver.Firefox(service=service, options=options)

# Abrir la URL
driver.get("https://www.360gradoslibros.es/contacto/")


# Localizar el campo de texto (nombre) por su ID
campo_nombre = driver.find_element(By.ID, "fname")

# Rellenar el campo con un nombre
campo_nombre.send_keys(nombre_completo)

# Localizar campo texto email
campo_email = driver.find_element(By.ID, "lname")

# Rellenar el campo email

campo_email.send_keys(email)


# Rellenar el campo email
#campo_email.send_keys("juan@ola.com")

# Localizar campo texto mensaje
campo_mensaje = driver.find_element(By.NAME,"subject" )

#Rellenar campo de texto mensaje
campo_mensaje.send_keys(mensaje_estructurado)

# Localizar el botón de enviar utilizando el XPath absoluto
boton_enviar = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/div/main/article/div/div/form/p[4]/input")

# Hacer clic en el botón de enviar
boton_enviar.click()

# Cerrar el navegador
driver.quit()



