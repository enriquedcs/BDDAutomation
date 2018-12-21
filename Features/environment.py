from selenium import webdriver
import os


def before_all(context):
    chromedriver = "C:\\Users\\\enriquealejandro.d\\\Documents\\Lib\\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    context.driver = webdriver.Chrome(chromedriver)
    context.driver.maximize_window()



def after_all(context):
    context.driver.close()
