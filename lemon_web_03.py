# -*- encoding:utf-8 -*-
# @Time : 2020/4/9 13:33 
# @Author : ZHH
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://hao123.com")
sleep(2)
# driver.maximize_window()
'''
获取元素文本内容
driver.find_element_by_xpath().text
获取元素属性
driver.find_element_by_xpath().get_attribute("name")
'''
#移动到元素的底端与当前窗口底部对齐
ele=driver.find_element_by_xpath('//a[@class="item  first active"]')
driver.execute_script("arguments[0].scrollIntoView(false);",ele)
sleep(1.5)
#元素的顶端与当前窗口顶部对其
driver.execute_script("arguments[0].scrollIntoView();",ele)
sleep(1.5)
#移动到页面底部
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(1.5)
#移动到页面顶部
driver.execute_script("window.scrollTo(document.body.scrollHeigth,0)")
