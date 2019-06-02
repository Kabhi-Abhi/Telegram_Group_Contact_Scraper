#!/usr/bin/env python3
# -*- encoding: utf-8

import time
from selenium import webdriver

phone_number = input("Enter your phone number: ")

chrome = webdriver.Chrome("./chromedriver.exe")
chrome.get("https://web.telegram.org/#/login")
time.sleep(5)

chrome.find_element_by_name("phone_number").send_keys(phone_number)

chrome.find_element_by_class_name("login_head_submit_wrap").click()

code = input("Enter Security Code: ")

chrome.find_element_by_class_name("btn btn-md btn-md-primary").click()

chrome.find_element_by_name("phone_code").send_keys(code)

groups = chrome.find_elements_by_class_name("im_dialog_wrap")

for i in range(len(groups)):
    print(f"{i}: {groups[i]}")

index = int(input("Enter the index of the group you wish to see: "))

groups[index].click()

chrome.find_elements_by_class_name("tg_head_btn").click()

chrome.delete_all_cookies()
chrome.quit()
