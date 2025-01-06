import random
from faker import Faker
from arranque import nombre_completo

# Crear una instancia de Faker
fake = Faker()

# Lista de dominios comunes
dominios = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com", "icloud.com"]






# Elegir un dominio aleatorio de la lista
dominio_email = random.choice(dominios)

# Crear el email completo
email = f"{nombre_completo}@{dominio_email}"

# Imprimir para depurar  
# #el email generado
print("email: " + email)

#rint(nombre)
#print(apellido)
print (nombre_completo)
