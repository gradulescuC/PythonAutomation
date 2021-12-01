import time

from behave import *
from selenium.webdriver.common.by import By


@given("I have cucumber installed")
def step_impl(context):
    print("Un mesaj important")

@when('Winter season is comming')
def step_impl(context):
    print("Prepare for impact")

@then('All tests should pass')
def step_impl(context):
    print("Good job")

print("---------------------------------------------------------------------")

@given("I go to autocomplete page")
def step_impl(context):
    context.browser.get("https://formy-project.herokuapp.com/")
    time.sleep(3)
    context.browser.find_element(By.LINK_TEXT,"Autocomplete").click()
    time.sleep(1)

@when('I type ko')
def step_impl(context):
    context.browser.find_element(By.ID,"autocomplete").send_keys("Craiova")

@then('Cluj-Napoca should be available')
def step_impl(context):
    print("Good job")
    time.sleep(3)

print("---------------------------------------------------------------------")

@given("I enter google.ro")
def step_impl(context):
    context.browser.get("https://google.ro")
    authorization = (By.CSS_SELECTOR,"#L2AGLb > div")
    context.browser.find_element(*authorization).click()

@when("I enter something in the text field")
def step_impl(context):
    search_bar = context.browser.find_element(By.NAME, "q")
    search_bar.send_keys("Flat Earth Society")
    search_bar.submit()

@then ("Results are displayed")
def step_impl(context):
    print("Search is complete")
    time.sleep(3)
    context.browser.quit()

print("-----------------------------------------------------------")


@given('I go to 4davanceboy to add item')
def step(context):
    context.browser.get('https://lambdatest.github.io/sample-todo-app/')

@then('I Click on first checkbox and second checkbox')
def click_on_checkbox_one(context):
    context.browser.find_element(By.NAME,'li1').click()
    context.browser.find_element(By.NAME,'li2').click()


@when('I enter item to add')
def enter_item_name(context):
    context.browser.find_element(By.ID,'sampletodotext').send_keys("Yey, Let's add it to list")


@when('I click add button')
def click_on_add_button(context):
    context.browser.find_element(By.ID,'addbutton').click()


@then('I should verify the added item')
def see_login_message(context):
    added_item = context.browser.find_element(By.XPATH,"//span[@class='done-false']").text
    time.sleep(10)
    if added_item in "Yey, Let's add it to list":
        return True
    else:
        return False