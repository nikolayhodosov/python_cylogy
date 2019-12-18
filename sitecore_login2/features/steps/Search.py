import os, time, random
from behave import given, then, when
from lib.Config import Config
from support.Search_Page import Search
from selenium.webdriver.common.keys import Keys


cf = Config()
sp = Search()


baaqmd_qa_eng = cf.get_config('config/config.ini', 'search', 'baaqmd_qa_eng')
baaqmd_prod_main_eng = cf.get_config('config/config.ini', 'search', 'baaqmd_prod_main_eng')

@given(u"I navigate to baaqmd main page")
def step_impl(context):
    #if (os.environ['location'] == "qa"):
       # context.browser.get(baaqmd_qa_eng)
    #elif (os.environ['location'] == "prod"):
        context.browser.get(baaqmd_prod_main_eng)

@when(u'I perform search for "{query}" query')
def step_impl(context, query):
    sp.search_field(context).clear()
    sp.search_field(context).send_keys(query)

@then(u'I perform search for "{query2}" query2')
def step_impl(context, query2):
    sp.search_field2(context).clear()
    sp.search_field2(context).send_keys(query2)

@then(u'I click Login button')
def step_impl(context):
    sp.login_button_click(context)

@then(u'I click Content Editor button from Launchpad')
def step_impl(context):
    sp.content_editor_click(context)

@then(u'I perform search for "{id1}" id1')
def step_impl(context, id1):
    sp.ce_search_field(context).clear()
    sp.ce_search_field(context).send_keys(id1 + Keys.ENTER)

@then(u'I click Send SMS button in Air District Tools tab')
def step_impl(context):
    sp.send_sms_click(context)

@then(u'I click Continue button in the SMS Message popup')
def step_impl(context):
    jquery_frame = context.browser.find_element_by_id("jqueryModalDialogsFrame")
    context.browser.switch_to_frame(jquery_frame)
    sms_frame = sp.sms_frame(context)
    context.browser.switch_to_frame(sms_frame)
    sp.sms_continue_button_click(context)

