Feature: Manipulate strings
  In order to have some fun
  As a programming beginner
  I want to manipulate strings

  Scenario: Introducimos Piscolabis
    Given I have the string "Piscolabis"
    When I put it in upper case
    Then I see the string is "{Piscolabis:1}"

  Scenario: Introducimos dos veces la misma palabra
    Given I have the string "Piscolabis Piscolabis"
    When I put it in upper case
    Then I see the string is "{Piscolabis:2}"

  Scenario: Introducimos dos palabras diferentes
    Given I have the string "Piscolabis Lettuce"
    When I put it in upper case
    Then I see the string is "{Piscolabis:1}, {Lettuce:1}"

  Scenario: Introducimos varias palabras repetidas y sin repetir
    Given I have the string "b b a a a c"
    When I put it in upper case
    Then I see the string is "{a:3}, {b:2}, {c:1}"

  Scenario: Introducimos mas de 100 caracteres
    Given I have the string "12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901"
    When I put it in upper case
    Then I see the string is "{1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890:1}"

  Scenario: Ejecutamos sin meter ninguna palabra
    Given I have the string ""
    When I put it in upper case
    Then I see the string is ""

