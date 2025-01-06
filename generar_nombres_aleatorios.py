from faker import Faker

# Crear una instancia de Faker en español
faker = Faker('en_US')

# Generar una lista de 1000 nombres completos
nombres_completos = [faker.name() for _ in range(1000)]

# Mostrar los primeros 10 nombres generados como ejemplo
print(nombres_completos[:10])

# Opcional: guardar la lista en un archivo de texto
with open("nombres_aleatorios.txt", "w") as archivo:
    archivo.write("\n".join(nombres_completos))
