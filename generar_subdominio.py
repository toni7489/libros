import random
from faker import Faker

# Crear una instancia de Faker
fake = Faker()

# Lista de dominios comunes
dominios = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com", "icloud.com"]



# Generar un nombre aleatorio para el email (primer nombre + apellido)
nombre_email = fake.first_name().lower() + "." + fake.last_name().lower()


nombre = fake.first_name()
apellido = fake.last_name()
nombre_email = nombre.lower() + "." + apellido.lower()
nombre_completo = nombre + " " + apellido


# Elegir un dominio aleatorio de la lista
dominio_email = random.choice(dominios)

# Crear el email completo
email = f"{nombre_email}@{dominio_email}"

# Imprimir el email generado
print("email: " + email)

print(nombre)
print(apellido)
print (nombre_completo)
