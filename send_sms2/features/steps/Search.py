import os, time, random
from behave import given, then, when
from lib.Config import Config
from support.Search_Page import Search
from selenium.webdriver.common.keys import Keys


cf = Config()
sp = Search()


baaqmd_qa_eng = cf.get_config('config/config.ini', 'search', 'baaqmd_qa_eng')
baaqmd_prod_main_eng = cf.get_config('config/config.ini', 'search', 'baaqmd_prod_main_eng')

@given(u"I navigate to STA SMS Form page")
def step_impl(context):
    #if (os.environ['location'] == "qa"):
       # context.browser.get(baaqmd_qa_eng)
    #elif (os.environ['location'] == "prod"):
        context.browser.get(baaqmd_prod_main_eng)

@when(u'I fill telephone number in phone field')
def step_impl(context):
    sp.phone_field_click(context)
    sp.phone_field(context).send_keys("1")
    sp.phone_field(context).send_keys("1231231234")

@then(u'I click Submit button')
def step_impl(context):
    sp.submit_button_click(context)
    time.sleep(10)

@then(u'I see Successfull message about SMS Form Submit')
def step_impl(context):
    print(sp.submit_message(context))
    assert sp.submit_message(context).is_displayed()