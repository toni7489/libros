from faker import Faker
from generar_subdominio import nombre_completo, email

# Crear una instancia de Faker
fake = Faker()

# Generar un mensaje estructurado
mensaje_estructurado = f"""
Hello, my name is {nombre_completo}.

I would like to know more about your product/service. I have been searching for information on your website and am interested in learning more details about the features, pricing, and how I could benefit from what you offer.

{fake.text(max_nb_chars=200)}

I appreciate your attention and I hope to receive a response soon.

Kind regards,
{nombre_completo}
"""

# Imprimir el mensaje generado
print(mensaje_estructurado)
print(email)
