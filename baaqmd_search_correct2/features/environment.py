import os, sys, time
from behave import *
from selenium import webdriver

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--acceptInsecureCerts')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-insecure-localhost')
    context.browser = webdriver.Chrome(chrome_options=options)
    context.browser.implicitly_wait(15)

def before_step(context, step):
    context.step = step
    src = context.browser.page_source

def after_scenario(context, scenario):
    context.browser.quit()
