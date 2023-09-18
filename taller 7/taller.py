from dataclasses import dataclass

@dataclass
class Elemento:
    nombre:str
    def __eq__(self, other):
        if isinstance (other, Elemento):
            return self.nombre==other.nombre
        else:
            return False
    
class Conjunto:

    contador=0
    def __init__(self,nombre:str):
        self.__id = Conjunto.contador
        Conjunto.contador += 1
        self.lista_elementos:list=[]
        self.nombre:str=nombre
    
    @property
    def id (self):
        return self.__id

    def Contiene (self, elemento:Elemento)->bool:
        for e in self.lista_elementos:
            if e == elemento:
                return True 
            else:
                return False 
    
    def agregar_elemento (self, elemento:Elemento):
        if not self.Contiene(elemento):
            self.lista_elementos.append(elemento)
        
    def unir (self, otro_conjunto:"Conjunto"):
        for elemento in otro_conjunto.lista_elementos:
            self.agregar_elemento(elemento)
    
    def __add__ (self, otro_conjunto:"Conjunto"):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNION {otro_conjunto.nombre}")
        nuevo_conjunto.lista_elementos = self.lista_elementos.copy()
        nuevo_conjunto.unir (otro_conjunto)
        return nuevo_conjunto
 
    @classmethod
    def intersectar (cls, conjunto_1:"Conjunto", conjunto_2:"Conjunto"):
        interseccion = Conjunto(f"{conjunto_1.nombre} INTERSECTADO {conjunto_2.nombre}")
        for elemento in conjunto_1.lista_elementos:
            if conjunto_2.contiene(elemento):
                interseccion.agregar_elemento(elemento)
        return interseccion

    def __str__ (self):
        elementos = ",".join (elemento.nombre for elemento in self.lista_elementos)
        return f"Comjunto {self.nombre}: ({elementos})"
    
