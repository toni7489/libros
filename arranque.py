import time
# Ejecutar el codigo 1000 veces cada 5 minutos
for i in range (1000):
    if 1<999: #contador de numero de ejecuciones
        with open('generar_subdominio.py') as f:
         exec(f.read())
        with open('generar_mensajes.py') as f:
         exec(f.read())
        with open('main.py') as f:
         exec(f.read())

        print ("Intento numero: " + str(i))  # Imprime el numero de intentos
        time.sleep(5*60) # 5 minutos en segundos





