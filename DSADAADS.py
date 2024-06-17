'''
repositorios en git hub poner newnew
    publico
    readme accionado
    definir lenguaje
    gitignore es para indicar el template
    y luego crear repositorio
    Una vez creado debemos llevarnos la ruta,donde dice code y nos llevamos el url https

luego en visual usamos git clone en la cosa de comandos y ponemos la ruta (el url)
con git add . vamos actualizando todo, si pones solo el nombre del programa en vez de punto pues es pasa eso especifico
luego si hago un git diff lo que esta en el disco debera ser igual que lo que esta en el dispositivo intermedio y esto te indica las diferencias, sino hay nada no sale nada
para subirlo al repositorio pones git commit -m "mensaje" y pones un mensaje
Luego de eso finalizas con git push
'''

import csv

lista = [['Daniel','22'],['Esteban','20'],['Benjamin','20']]
with open("archivo.csv",'w') as f:
    escritor = csv.writer(f,delimiter=";")
    escritor.writerow(['Nombre','Edad'])
    for x in lista:
        escritor.writerow(x)
        escritor.writerow("Hola gente")
