import unittest
from mock import patch, Mock

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pdb

import SimpleHTTPServer
import SocketServer


class TestStringsExamples(unittest.TestCase):

    def test_una_palabra(self):
        textWords = "Piscolabis"

        driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        driver.get("http://localhost:8080/www/")

        text = driver.find_element_by_name("text")

        reset = driver.find_element_by_id("reset")
        execute = driver.find_element_by_id("execute")

        text.send_keys(textWords)
        execute.send_keys("\n")

        p1 = driver.find_element_by_id("p1")
        p2 = driver.find_element_by_id("p2")

        assert p1.text == "{Piscolabis:1}"
        assert p2.text == "1"

        driver.close()

    def test_reset_con_execute(self):
        textWords = "Piscolabis"

        driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        driver.get("http://localhost:8080/www/")
        text = driver.find_element_by_name("text")

        reset = driver.find_element_by_id("reset")

        execute = driver.find_element_by_id("execute")

        text.send_keys(textWords)

        execute.send_keys("\n")

        reset.send_keys("\n")

        p1 = driver.find_element_by_id("p1")
        p2 = driver.find_element_by_id("p2")

        assert p1.text == ""
        assert p2.text == ""

        driver.close()

    def test_reset_sin_execute(self):
        textWords = "Piscolabis"

        driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        driver.get("http://localhost:8080/www/")
        text = driver.find_element_by_name("text")

        reset = driver.find_element_by_id("reset")

        text.send_keys(textWords)

        reset.send_keys("\n")

        p1 = driver.find_element_by_id("p1")
        p2 = driver.find_element_by_id("p2")

        assert p1.text == ""
        assert p2.text == ""

        driver.close()

    def test_ordenar(self):
        textWords = "b b a a a c"

        driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        driver.get("http://localhost:8080/www/")

        text = driver.find_element_by_name("text")

        execute = driver.find_element_by_id("execute")

        text.send_keys(textWords)
        execute.send_keys("\n")

        p1 = driver.find_element_by_id("p1")
        p2 = driver.find_element_by_id("p2")

        assert p1.text == "{a:3}, {b:2}, {c:1}"

        driver.close()

    def test_contar_total(self):
        textWords = "b b a a a c"

        driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        driver.get("http://localhost:8080/www/")

        text = driver.find_element_by_name("text")

        execute = driver.find_element_by_id("execute")

        text.send_keys(textWords)
        execute.send_keys("\n")

        p1 = driver.find_element_by_id("p1")
        p2 = driver.find_element_by_id("p2")

        assert p2.text == "3"

        driver.close()

    def test_contar_palabra(self):
        textWords = "a a a a a"

        driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        driver.get("http://localhost:8080/www/")

        text = driver.find_element_by_name("text")

        execute = driver.find_element_by_id("execute")

        text.send_keys(textWords)
        execute.send_keys("\n")

        p1 = driver.find_element_by_id("p1")
        p2 = driver.find_element_by_id("p2")

        assert p1.text == "{a:5}"

        driver.close()

    def test_mas_de_100_caracteres(self):
        textWords = "12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901"

        driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        driver.get("http://localhost:8080/www/")

        text = driver.find_element_by_name("text")

        execute = driver.find_element_by_id("execute")

        text.send_keys(textWords)
        execute.send_keys("\n")

        p1 = driver.find_element_by_id("p1")
        p2 = driver.find_element_by_id("p2")

        assert p1.text == "{1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890:1}"

        driver.close()

if __name__ == '__main__':

    # unittest.main()
