import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Search:
    def phone_field(self, context):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='fxb_00000000-0000-0000-0000-000000000000_Fields_e5d60e93-f6e9-4a9f-aa43-370a20043778__Value']")))
        return context.browser.find_element_by_xpath("//*[@id='fxb_00000000-0000-0000-0000-000000000000_Fields_e5d60e93-f6e9-4a9f-aa43-370a20043778__Value']")

    def phone_field_click(self, context):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='fxb_00000000-0000-0000-0000-000000000000_Fields_e5d60e93-f6e9-4a9f-aa43-370a20043778__Value']")))
        context.browser.find_element_by_xpath("//*[@id='fxb_00000000-0000-0000-0000-000000000000_Fields_e5d60e93-f6e9-4a9f-aa43-370a20043778__Value']").click

    def submit_button_click(self, context):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='fxb.00000000-0000-0000-0000-000000000000.6bc2fbf1-273d-4b89-a477-63ce0be7ed06']")))
        context.browser.find_element_by_xpath("//*[@name='fxb.00000000-0000-0000-0000-000000000000.6bc2fbf1-273d-4b89-a477-63ce0be7ed06']").click()

    def submit_message(self, context):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//p[@class='sign-up-notifications__toolbar-description-on-submit'][contains(text(),'Thank you')]")))
        return context.browser.find_element_by_xpath("//p[@class='sign-up-notifications__toolbar-description-on-submit'][contains(text(),'Thank you')]")