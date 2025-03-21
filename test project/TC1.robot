*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Test Cases ***
LoginTest

    #Create Webdriver chrome

    open    https://demo.nopcommerce.com/login?returnUrl=%2Fregisterresult%2F1

    click element  Xpath://*[@class="ico-login"]

    input text  id:Email    nr785849@gmail.com

    input text   id:Password 6301945225

    click element   Xpath://*[@class="button-1 login-button"]

    close browser

