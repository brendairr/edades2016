Feature: Devuelve mensaje por edad dada.
	Como usuario del sistema edades
	quiero ingresar una edad y me regrese un mensaje segun mi edad
	para tener siempre presente mis años

	Scenario: Con edad igual o menor a -1
		Dado que ingreso la edad "-1" 
		cuando consulto mi mensaje
		entonces veo "no existes"

	Scenario: Con edad igual o menor a 12 pero mayor a 0
		Dado que ingreso la edad "8"
		cuando consulto mi mensaje
		entonces veo "eres niño"

	Scenario: Con edad igual o menor a 18 pero mayor a 12
		Dado que ingreso la edad "15"
		cuando consulto mi mensaje
		entonces veo "eres adolescente"

	Scenario: Con edad igual o menor a 64 pero mayor a 18
		Dado que ingreso la edad "48"
		cuando consulto mi mensaje
		entonces veo "eres adulto"
	
	Scenario: Con edad igual o menor a 119 pero mayor a 64
		Dado que ingreso la edad "83"
		cuando consulto mi mensaje
		entonces veo "eres adulto mayor"

	Scenario: Con edad mayor a 119
		Dado que ingreso la edad "225"
		cuando consulto mi mensaje
		entonces veo "eres Mumm-Ra"

	Scenario: Con edad igual a hg
		Dado que ingreso la edad "hg"
		cuando consulto mi mensaje
		entonces veo "El valor que ingresaste es incorrecto, ingresa solo numeros por favor"