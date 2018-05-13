Feature: Cantidad palabras
  In Metemos palabra Piscolabis
  As Pulsando ejecutar
  I Vemos el string 1

  Scenario: Introducimos una palabra
    Given I have the string "Piscolabis"
    When Pulsamos ejecutar
    Then I see the number is 1

  Scenario: Introducimos varias palabras
    Given I have the string "b b a a a c"
    When Pulsamos ejecutar
    Then I see the number is 3

