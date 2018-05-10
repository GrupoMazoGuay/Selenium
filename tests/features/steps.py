from lettuce import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pdb


@step('Pasamos el string (\s+)')
def have_the_number(step, string):
    textWords = string

    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get("http://localhost:8080/")

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


@step('I compute its factorial')
def compute_its_factorial(step):
    world.number = factorial(world.number)


@step('I see the number (\d+)')
def check_number(step, expected):
    expected = int(expected)
    assert world.number == 1, \
        "Got %d" % world.number


def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)
