# environment.py e un fisier required de cucumber
from selenium import webdriver

def before_all(context):
    context.browser=webdriver.Chrome("/04 - selenium_workshop_pom/resources/chromedriver")

def after_all(context):
    context.browser.quit()  # context  e un parametru caruia ii definesc anumite variabile ce sunt citite doar atunci cand avem nevoie
                            # cu acest context vom face legatura cu testele noastre
    print("trecem pe aici")