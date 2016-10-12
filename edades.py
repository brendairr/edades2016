# -*- coding: utf-8 -*-
class Edades:
	def mensaje(self, edad):  #cada que creamos una función(método) dentro de la clase hay que escribir self
		
		try: 
			edad = int (edad)
			if edad < 0: 
				return "no existes"

			elif (edad > 0) and (edad <= 12):
				return u"eres niño"

			elif (edad > 12) and (edad <= 18):
				return "eres adolescente"

			elif (edad > 18) and (edad <= 64):
				return "eres adulto"

			elif (edad > 64) and (edad <= 119):
				return "eres adulto mayor"

			elif (edad > 119):
				return "eres Mumm-Ra"

		except: 
			return "El valor que ingresaste es incorrecto, ingresa solo numeros por favor"

		