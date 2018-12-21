from behave import *
from selenium import webdriver
import os
import time



@given('User is on registration page')
def user_reg_page(context):
    # Set chrome driver
    context.driver.get("http://qa1.smbstaging.com/")
    context.driver.find_element_by_xpath("//span[contains(text(),'My Account')]").click()
    time.sleep(8)


@when('User enters username')
def enter_username(context):
    context.driver.find_element_by_id("edit-name").send_keys("enrique.decoss@wolterskluwer.com")



@when('User enters password')
def enter_password(context):
    context.driver.find_element_by_id("edit-pass").send_keys("Today123")


@when('User enters invalid password')
def enter_password(context):
    context.driver.find_element_by_id("edit-pass").send_keys("Today1234")


@when('User click on signup button')
def click_signup(context):
    context.driver.find_element_by_id("edit-submit").click()



@then('User should be logged successfully')
def validation_success(context):
    print("Login valid")


@when('User enters invalid username')
def enter_username(context):
    context.driver.find_element_by_id("edit-name").send_keys("invalid.test@wolterskluwer.com")


@then('User should NOT be registered successfully')
def validation_success(context):
    print("Invalid login")