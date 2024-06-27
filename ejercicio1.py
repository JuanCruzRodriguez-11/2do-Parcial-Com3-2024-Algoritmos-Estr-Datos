import datetime
import random

class Fecha:
    def __init__(self, dd, mm, aaaa):
        self.dd = dd
        self.mm = mm
        self.aaaa = aaaa
    def __str__(self):
        return f"{self.dd}/{self.mm}/{self.aaaa}"

    def __add__(self, other):
        dias = self.dd + other.dd
        meses = self.mm + other.mm
        anios = self.aaaa + other.aaaa
        return Fecha(dias, meses, anios)

    def __eq__(self, other):
        return self.dd == other.dd and self.mm == other.mm and self.aaaa == other.aaaa

    def calcular_dif_fecha(self, other):
        dias = abs(self.dd - other.dd)
        meses = abs(self.mm - other.mm)
        anios = abs(self.aaaa - other.aaaa)
        return f"{dias} dias, {meses} meses y {anios} años"
      
class Alumno(dict):
  def __init__(self, nombre, dni, fecha_ingreso, carrera):
    self["Nombre"] = nombre
    self["DNI"] = dni
    self["FechaIngreso"] = fecha_ingreso
    self["Carrera"] = carrera

  def cambiar_datos(self, **kwargs):
    for key, value in kwargs.items():
      self[key] = value

  def antiguedad(self):
    hoy = datetime.date.today()
    return hoy - self["FechaIngreso"]

  def __str__(self):
    return f"Alumno: {self['Nombre']}, DNI: {self['DNI']}, Carrera: {self['Carrera']}"

  def __eq__(self, other):
    if not instance(other, Alumno):
     return self["DNI"] == other["DNI"]

alumno1 = Alumno("Juan", 35123456, datetime.date(2020, 3, 15), "Ingeniería")

alumno1.cambiar_datos(Nombre="Juan Gomez", Carrera="Ingenieria")

class Alumno:
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self.nombre = nombre
        self.dni = dni
        self.fecha_ingreso = fecha_ingreso
        self.carrera = carrera

class Nodo:
    def __init__(self, alumno):
        self.alumno = alumno
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar_alumno(self, alumno):
        nodo = Nodo(alumno)
        if self.primero is None:
            self.primero = nodo
            self.ultimo = nodo
        else:
            nodo.anterior = self.ultimo
            self.ultimo.siguiente = nodo
            self.ultimo = nodo

    def lista_ejemplo(self, cantidad_alumnos):
        lista_alumnos = ListaDoblementeEnlazada()
        for _ in range(cantidad_alumnos):
            nombre = "Alumno" + str(_)
            dni = random.randint(10000000, 99999999)
            fecha_ingreso = random.randint(2000, 2022) 
            carrera = "Informática"
            alumno = Alumno(nombre, dni, fecha_ingreso, carrera)
            lista_alumnos.agregar_alumno(alumno)
        return lista_alumnos

    def __iter__(self):
        return IteradorAlumno(self)
    
    def ordenar_por_fecha_ingreso(self):
        nodos = []
        nodo_actual = self.primero
        while nodo_actual is not None:
            nodos.append(nodo_actual)
            nodo_actual = nodo_actual.siguiente

        nodos.sort(key=lambda x: x.alumno.fecha_ingreso)

        lista_ordenada = ListaDoblementeEnlazada()
        for nodo in nodos:
            lista_ordenada.agregar_alumno(nodo.alumno)
        
        return lista_ordenada

class IteradorAlumno:
    def __init__(self, lista):
        self.lista = lista
        self.nodo_actual = lista.primero

    def __iter__(self):
        return self

    def __next__(self):
        if self.nodo_actual is None:
            raise StopIteration
        else:
            alumno = self.nodo_actual.alumno
            self.nodo_actual = self.nodo_actual.siguiente
            return alumno


lista_alumnos = ListaDoblementeEnlazada().lista_ejemplo(5)
lista_ordenada = lista_alumnos.ordenar_por_fecha_ingreso()




