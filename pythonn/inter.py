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
