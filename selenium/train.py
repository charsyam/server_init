# -*- coding: utf-8 -*- 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys

id = sys.argv[1]
pw = sys.argv[2]
num = sys.argv[3]
month = sys.argv[4]
day = sys.argv[5]


driver = webdriver.Firefox()
try:
    driver.get("http://www.korail.com/2012/index.jsp")
    driver.find_element_by_link_text("로그인").click()
    driver.find_element_by_name('txtMember').send_keys(id)
    driver.find_element_by_name('txtPwd').send_keys(pw)
    driver.find_element_by_name("imgConfirm").click()
    alert = driver.switch_to_alert()
    time.sleep(2)
    alert.accept()

    driver.get("http://www.korail.com/2012/index.jsp")
    select = driver.find_element_by_name("txtPsgFlg_1")
    options = select.find_elements_by_tag_name("option")
    for option in options:
        if num == option.get_attribute("value"):
            option.click()

    select = driver.find_element_by_name("selGoMonth")
    options = select.find_elements_by_tag_name("option")
    for option in options:
        print option.get_attribute("value")
        if month == option.get_attribute("value"):
            option.click()

    select = driver.find_element_by_name("selGoDay")
    options = select.find_elements_by_tag_name("option")
    for option in options:
        if day == option.get_attribute("value"):
            option.click()
#driver.find_element_by_xpath("//select[@name='selGomonth']/option[text()='9']").select()
#driver.find_element_by_xpath("//select[@name='selGoDay']/option[text()='14']").select()

#driver.find_element_by_name("btnRsv1_3").click()
    #driver.find_element_by_css_selector('img[alt=&quot;조회하기&quot;]').click()
    gobtn = driver.find_element_by_xpath("//img[@alt='조회하기']")
    gobtn.click()

    time.sleep(10)
    driver.close()
except:
    print "Unexpected error:", sys.exc_info()[0]    
    driver.close()


