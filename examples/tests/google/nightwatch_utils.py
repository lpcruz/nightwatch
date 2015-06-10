# -*- coding: utf-8 -*-
# !/usr/bin/env python
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

test_name = "Google Test"

print "Starting " + test_name
print "======================"
print ""

driver_path='/Users/lcruz/Desktop/lcruz/Projects/nightwatch/chromedriver'
start_time = time.time()

def driver(driver_path):
    return webdriver.Chrome(executable_path=driver_path)
