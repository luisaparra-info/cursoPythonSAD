import sys

class Superheroe(): #Creamos la clase Humano
    superhero = ''
    publisher = ''
    alter_ego = ''
    first_appearance = ''
    characters = ''

    def __init__(self='', superhero='', publisher='', alter_ego='', first_appearance='',characters=''):
        self.superhero = superhero
        self.publisher = publisher
        self.alter_ego = alter_ego
        self.first_appearance = first_appearance
        self.characters = characters

    
    @staticmethod
    def cargarLista(lista):
        listaSuperheroes=[]
        for s in lista:   
            superhero=s["superhero"]
            publisher=s["publisher"]   
            alter_ego=s["alter_ego"]   
            first_appearance=s["first_appearance"]   
            characters=s["characters"]   
            listaSuperheroes.append(Superheroe(superhero,publisher,alter_ego,first_appearance,characters))

        return listaSuperheroes
    
    @staticmethod
    def numSuperheroes(lista):
        return len(lista)

    def buscarPorNombre(lista,nombre):
        for l in lista:
            #print(isinstance(l,Superheroe))
            if l.superhero.lower() == nombre.lower():
                return l
        return 