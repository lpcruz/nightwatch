# -*- coding: utf-8 -*-
# !/usr/bin/env python
'''Below is a template for setting up the utils'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, re
import time
import os
import sys

'''The Above module imports DO NOT change'''

test_name = "Your Test Name "

print "Runnning " + test_name
print "======================"
print ""

driver_path= os.getcwd() + '/chromedriver'
start_time = time.time()

def driver(driver_path):
    return webdriver.Chrome(executable_path=driver_path)
