import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Search:
    def search_field(self, context):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='UserName']")))
        return context.browser.find_element_by_xpath("//*[@id='UserName']")

    def search_field2(self, context):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='Password']")))
        return context.browser.find_element_by_xpath("//*[@id='Password']")

    def login_button_click(self, context):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='LogInBtn']")))
        context.browser.find_element_by_xpath("//*[@id='LogInBtn']").click()

    def content_editor_click(self, context):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@title='Content Editor']")))
        context.browser.find_element_by_xpath("//*[@title='Content Editor']").click()

    def ce_search_field(self, context):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='TreeSearch']")))
        return context.browser.find_element_by_xpath("//*[@id='TreeSearch']")

    def send_sms_click(self, context):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@title='Send SMS']")))
        context.browser.find_element_by_xpath("//*[@title='Send SMS']").click()

    def sms_continue_button_click(self, context):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.ID, "continueButton")))
        context.browser.find_element_by_id("continueButton").click()

    def sms_frame(self, context):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.ID, "scContentIframeId0")))
        return context.browser.find_element_by_id("scContentIframeId0")

    def search_result_query(self, context, query):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='outercontent_1_sidenavigationcontainercontent_1_litSearchResults']")))
        return context.browser.find_element_by_xpath("//*[@id='outercontent_1_sidenavigationcontainercontent_1_litSearchResults'][contains(text(), \"" + query + "\")]")

    def search_results_header2(self, context, refine_query):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='result']//h3[@class='search-result-header__title'][contains(text(), \"" + refine_query + "\")]")))
        return context.browser.find_element_by_xpath("//*[@id='result']//h3[@class='search-result-header__title'][contains(text(), \"" + refine_query + "\")]")

    def search_results_query_name(self, context, refine_query):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='outercontent_1_sidenavigationcontainercontent_1_litSearchResults'][contains(text(), \"" + refine_query + "\")]")))
        return context.browser.find_element_by_xpath("//*[@id='outercontent_1_sidenavigationcontainercontent_1_litSearchResults'][contains(text(), \"" + refine_query + "\")]")

    def search_results_query_count(self, context, refine_query):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='outercontent_1_sidenavigationcontainercontent_1_litSearchResults'][contains(text(), \"" + refine_query + "\")]")))
        return context.browser.find_element_by_xpath("//*[@id='outercontent_1_sidenavigationcontainercontent_1_litSearchResults'][contains(text(), \"" + refine_query + "\")]")

    def search_results_search_field(self, context, refine_query):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.ID, "outercontent_1_sidenavigationcontainercontent_1_txtSearch")))
        return context.browser.find_element_by_id("outercontent_1_sidenavigationcontainercontent_1_txtSearch")

    def search_results_1st_card_text(self, context):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@class='emph'][1]/div[@class='result-content dynamic-overlay-container']/a")))
        return context.browser.find_element_by_xpath("//*[@class='emph'][1]/div[@class='result-content dynamic-overlay-container']/a").text

    def search_results_1st_card(self, context, refine_query):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@class='emph'][1]/div[@class='result-content dynamic-overlay-container']/a[contains(text(), \"" + refine_query + "\")]")))
        return context.browser.find_element_by_xpath("//*[@class='emph'][1]/div[@class='result-content dynamic-overlay-container']/a[contains(text(), \"" + refine_query + "\")]").text

    def search_results_1st_card_click(self, context, query):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@class='emph'][1]/div[@class='result-content dynamic-overlay-container']/a[contains(text(), \"" + query + "\")]")))
        context.browser.find_element_by_xpath("//*[@class='emph'][1]/div[@class='result-content dynamic-overlay-container']/a[contains(text(), \"" + query + "\")]").click()

    def search_results_selected_headline(self, context):
        WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#outercontent_1_sidenavigationcontainercontent_0_pnlPageTitle h1")))
        return context.browser.find_element_by_css_selector("#outercontent_1_sidenavigationcontainercontent_0_pnlPageTitle h1").text