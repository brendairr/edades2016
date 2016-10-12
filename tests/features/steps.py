# -*- coding: utf-8 -*-
from lettuce import step, world #world hace las variables visibles en todos los métodos steps(globales)
from edades import Edades	

@step(u'cuando consulto mi mensaje')
def cuando_consulto_mi_mensaje(step):
    pass    

# en features lo que está entrecomillado los agarra como parámetro

@step(u'Dado que ingreso la edad "([^"]*)"')
def dado_que_ingreso_la_edad_group1(step, edad1):
    edad = Edades()
    world.mensaje = edad.mensaje(edad1)

@step(u'entonces veo "([^"]*)"')
def entonces_veo_group1(step, mensaje_esperado):
    assert world.mensaje == mensaje_esperado, \
     ' Mensaje esperado' + mensaje_esperado + ' y se obtuvo ' + world.mensaje
