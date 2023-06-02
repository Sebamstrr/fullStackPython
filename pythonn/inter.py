x = [[5, 2, 3], [10, 8, 9]]
estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
directorio_deportes = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# Cambiar el valor 10 en x a 15
x[1][0] = 15
print(x)  # [[5, 2, 3], [15, 8, 9]]

# Cambiar el "apellido" del primer alumno de 'Jordan' a 'Bryant'
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)  # [{'first_name': 'Michael', 'last_name': 'Bryant'}, {'first_name': 'John', 'last_name': 'Rosales'}]

# En el directorio_deportes, cambiar "Messi" por "Andrés"
directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)  # {'basketball': ['Kobe', 'Jordan', 'James', 'Curry'], 'fútbol': ['Andrés', 'Ronaldo', 'Rooney']}

# Cambiar el valor 20 en z a 30
z[0]['y'] = 30
print(z)  # [{'x': 10, 'y': 30}]

estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterateDictionary(some_list):
    for item in some_list:
        for key, value in item.items():
            print(f"{key} - {value}")

iterateDictionary(estudiantes)
# Salida:
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(item[key_name])

iterateDictionary2('first_name', estudiantes)
# Salida:
# Michael
# John
# Mark
# KB

iterateDictionary2('last_name', estudiantes)
# Salida:
# Jordan
# Rosales
# Guillen
# Tonel

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{len(value)} {key.upper()}")
        for item in value:
            print(item)

