from lettuce import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pdb


from lettuce import *


@step('I have the string "(.*)"')
def have_the_string(step, string):
    world.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    world.driver.get("http://localhost:8080/")
    text = world.driver.find_element_by_name("text")
    text.send_keys(string)
    world.string = string


@step
def i_put_it_in_upper_case(step):
    reset = world.driver.find_element_by_id("reset")
    execute = world.driver.find_element_by_id("execute")
    execute.send_keys("\n")
    p1 = world.driver.find_element_by_id("p1")
    world.string = p1.text


@step
def see_the_string_is(step, expected):
    '''I see the string is "(.*)"'''
    assert world.string == expected
    world.driver.close()


@step
def see_the_number_is(step, expected):
    '''I see the number is (\d+)'''
    assert world.string == expected
    world.driver.close()


@step('Pulsamos ejecutar')
def pulsamos_ejecutar(step):
    reset = world.driver.find_element_by_id("reset")
    execute = world.driver.find_element_by_id("execute")
    execute.send_keys("\n")
    p2 = world.driver.find_element_by_id("p2")
    world.string = p2.text
