Feature: Computamos una palabra
	Para computar una palabra
	Como usuario
	Vamos a procesar un string con una sola palabra

    Scenario: Computar "Piscolabis"
        Given Pasamos el string Piscolabis
        When I compute its factorial
        Then I see the number 1
