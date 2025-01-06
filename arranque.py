import time

# Lista de nombres
nombres = [
    "Diana Reyes", "Richard Williams", "Amy Gomez", "James Jordan", "Nicole Davis",
    "Natasha Reyes", "Paul Todd", "Alan Moreno", "Tonya Davidson", "Eric Velasquez",
    "Raymond Greer", "Lisa Sutton", "Robert Thomas", "Tricia Moody", "Joseph Miller",
    "Cindy Ray", "Jessica Tate", "Kathleen Ryan", "James Leach", "Ray Wood",
    "Kiara Jones", "Mallory Reynolds", "Ebony Taylor", "Caleb Browning", "Kelly Rivera",
    "Katie Davenport", "Corey Mcgrath", "Dawn Brooks", "Holly Benitez", "Sandra Johnson",
    "Kathleen Chaney", "Lisa Savage", "Ronald Wilkins", "Matthew Pollard", "Daniel Williams",
    "Heather Mayo", "Megan Reed", "Rebecca Jenkins", "Ashley Stewart", "William Hopkins",
    "Eric Burke", "Crystal Lee", "Sara Proctor", "Michael Rodriguez", "Victoria Wilson",
    "Julie Marquez", "Peggy Johnson", "Michelle Barber", "Catherine Brown", "Rachel Foley",
    "Rebecca Lopez", "Amy Palmer", "Matthew Anderson", "Aimee Hernandez", "Raven Jenkins",
    "Jordan Watson", "John Harper", "Alexander Gonzalez", "Sean Gonzalez", "Stephen Parker",
    "Michael Hoffman", "Pamela Bush", "Andrew Harrison", "Jeremy Suarez", "Megan Oconnor",
    "Christine Pratt", "Michael Chang", "Monica James", "Thomas Peterson", "Rita Wyatt MD",
    "Jonathan Bowman", "Brian Mendez", "Aimee Williams", "Elizabeth Harrison", "Angela Moss",
    "Stephanie Crawford", "Derek Saunders", "John Miller", "Derrick Murphy", "Leah Carpenter",
    "Michael Clayton", "Joshua Garrett", "Troy Gonzales", "James Jones", "Leonard Cook",
    "Cynthia Stanley", "Alison Ferguson", "Amanda Padilla", "Cynthia Day", "Eric Williams",
    "Shannon Jones", "Jessica Colon", "Sarah Singleton", "Kelly Novak", "James Allen",
    "Richard Mcdonald", "Brian Dunn", "Mrs. Sarah Eaton MD", "Stacy Dalton", "Cassidy Williams",
    "Melanie Griffin", "Nicholas Lee", "Amy Hodges", "Matthew White", "Amanda Dunn",
    "Holly Doyle", "David Bryant", "Calvin Walker", "Christopher Larson", "Melissa Wood",
    "Ann Robertson", "Keith Mercado", "Michael Allen", "Jasmine Smith", "Michele Jackson",
    "Jonathan Cabrera", "Alexis Rodriguez", "Dana Reese", "Jeremy Smith", "Kenneth Smith",
    "Brandon Wiggins", "Bobby Allen", "Taylor Mcclain", "James Lopez", "Stephen Sanchez",
    "Emma Rowe", "Ian Thomas", "Wendy Kaiser", "Jennifer Farmer", "Jennifer Guerra",
    "Randall Smith", "Maria Lucas DVM", "Erin Hamilton", "Nancy Nunez", "Robert Williams",
    "Paige Mendoza", "Lee Aguilar", "Natalie Case", "Crystal Rangel", "Tina Harris",
    "Brandon Smith", "David Stephens", "Kevin Schmidt", "Brandon Sutton", "Jacqueline Morgan",
    "Angela Bell", "Jacqueline Castillo", "Seth Velasquez", "Kim Bishop", "Ashley Lopez",
    "Michael Gilbert", "David Brandt", "Samuel Miller", "Amanda Skinner", "Robert Henderson",
    "Kathleen Martinez", "Patricia Thompson", "Christopher Jones", "Victoria Jackson", "Michael Silva",
    "Nicholas Serrano", "Angelica King", "Stefanie Wood", "Diana Jordan", "Kathryn Rivera",
    "Christine Good", "Steven Gill", "Helen Bennett", "Michael Reed", "Amy Stanley",
    "Jessica Johnson", "Victoria Anderson", "John Roth", "Michael Estrada", "Michele Shea",
    "Joe Alvarado", "Stephen Roberts", "Brianna West", "Jessica Kaiser", "Katherine Johnson",
    "Jill Collins", "Alan Rodriguez", "Jason Duran", "Jerry Green", "Rachel Thompson",
    "Luis Olson", "Melissa Peterson", "David Turner", "Nathaniel Brown", "Leslie Brown",
    "Michelle Calderon", "Sara Robles", "Scott Davis", "Ronald Harris", "Tyler Shelton",
    "Kenneth Webster", "Sara Davis", "Randy Hicks", "Corey Baldwin", "Leslie Vasquez",
    "Amanda Garcia", "Keith Vance", "Cameron Smith", "Rachel Harris", "Melanie Green",
    "James Martinez", "Diane Graham", "Christopher Bishop", "Sally Jones", "Joyce Avila DDS",
    "William Diaz", "Jacqueline Spence", "Kenneth Wilson", "Heidi Andrews", "George Brock",
    "Yvonne Hart", "Matthew Hensley", "Jasmine Kirk", "George Daugherty", "Kevin Jones",
    "Sheila Rodriguez", "Mary Gonzalez", "Laura Torres", "Michael Crane", "Ana Pena",
    "Leonard Snyder", "Sharon Hernandez", "David Little", "David Kim", "Raymond Pena",
    "Jeff Crawford", "Donna Knight", "Lonnie Jacobson", "Scott Cox", "Matthew Bishop",
    "Paula Rowe", "Kimberly Hansen", "Gregory Fuentes", "Ryan Williams", "Marissa Salazar",
    "Laura Brennan", "Kevin David", "Michael Garcia", "Nathaniel Cortez", "Laura Rivera",
    "Mark Clark", "Joshua Wilson", "Kelly Young", "Catherine Thomas", "Kayla Fuentes",
    "Courtney Sullivan", "Jonathan Martin", "Brian Rodriguez", "Benjamin White", "Jennifer Wheeler",
    "Rachel Williams", "Amy Gutierrez", "Tammy Brooks", "Bonnie Higgins", "Denise Lopez",
    # (Continuación completa...)
]


# Asegúrate de que la longitud de la lista sea suficiente
total_nombres = len(nombres)

# Asegurando que no haya más de 1000 ejecuciones
for i in range(1, total_nombres):  # Limitar a un máximo de 1000 ejecuciones
    
    nombre_completo = nombres[i]
    

    try:
        with open('generar_subdominio.py') as f:
            exec(f.read())
        with open('main.py') as f:
            exec(f.read())
    except FileNotFoundError as e:
        print(f"Error al abrir el archivo: {e}")
    except Exception as e:
        print(f"Se produjo un error durante la ejecución: {e}")

    print(f"Ejecutado intento número: {i} con el nombre: {nombre_completo}")    

    # Dormir 5 minutos (300 segundos)
    time.sleep(5 * 60)

# Si quieres una notificación cuando se termine el bucle
print("Se han procesado todos los nombres.")
