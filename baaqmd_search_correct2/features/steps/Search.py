import os, time, random
from behave import given, then, when
from lib.Config import Config
from support.Search_Page import Search
from selenium.webdriver.common.keys import Keys
import requests


cf = Config()
sp = Search()


baaqmd_qa_eng = cf.get_config('config/config.ini', 'search', 'baaqmd_qa_eng')
baaqmd_prod_main_eng = cf.get_config('config/config.ini', 'search', 'baaqmd_prod_main_eng')

@given(u"I navigate to baaqmd main page")
def step_impl(context):
    #if (os.environ['location'] == "qa"):
       # context.browser.get(baaqmd_qa_eng)
    #elif (os.environ['location'] == "prod"):
       # context.browser.get(baaqmd_prod_main_eng)
        requests.get('http://dev-sa-baaqmd.cylogy.com/admin/twiliosms/SendMessage', auth=('cylogy', 'dev@1234'))
        time.sleep(10)


@when(u'I perform search for "{query}" query')
def step_impl(context, query):
    sp.search_field(context).clear()
    sp.search_field(context).send_keys(query + Keys.ENTER)

@then(u'I see relevant results returned for "{query}" query')
def step_impl(context, query):
    print(sp.search_result_query(context, query))
    assert sp.search_result_query(context, query).is_displayed()

@then(u'I refine query on Search page and check the relevance of the result')
def step_impl(context):
    refine_query = sp.search_results_1st_card_text(context)
    print(refine_query)
    sp.sp.search_result_query(context).clear()
    sp.sp.search_result_query(context).send_keys(refine_query + Keys.ENTER)
    print(sp.search_results_query_name(context, refine_query))
    assert sp.search_results_query_name(context, refine_query).is_displayed()

@then(u'I check the first card from the results')
def step_impl(context):
    result_card_1 = sp.search_results_1st_card(context)
    sp.search_results_1st_card_click(context)
    time.sleep(3)
    print(sp.search_results_selected_headline(context))
    assert sp.search_results_selected_headline(context) == result_card_1