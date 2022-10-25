from webbrowser import get
import funciones_calculadora
import requests
from superheroe import Superheroe

'''
funciones_calculadora.calculadora()

'''
import requests
url = 'https://api.jsonbin.io/v3/b/6357f1152b3499323bea331b'
headers = {
  'X-Master-Key': '$2b$10$WMUuYfEWi/jIZHSqBOtzF.tCad3nJvyYYvXU8jR6zmVbU5RAlAILu'
}
req = requests.get(url, json=None, headers=headers)
#print(req.text)
superheroes=req.json()["record"]
listaSuperheroes=Superheroe.cargarLista(superheroes)
print(len(listaSuperheroes))

print('Introduce nombre del superheroe')
nombre = input()
s = Superheroe.buscarPorNombre(listaSuperheroes,nombre)

if isinstance(s,Superheroe): 
  print(s.alter_ego)
else: 
  print('No se ha encontrado')