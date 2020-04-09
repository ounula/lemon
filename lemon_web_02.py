# -*- encoding:utf-8 -*-
# @Time : 2020/4/9 11:00 
# @Author : ZHH
from selenium import webdriver
from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.by import By
#导入select 库
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
#找到鼠标要操作的元素
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//following::div[@id="u1"]/a[@class ="pf"]')))
ele = driver.find_element_by_xpath('//following::div[@id="u1"]/a[@class ="pf"]')
# #实例化ActionChains类
# ac=ActionChains(driver)
# #将鼠标操作添加到actions列表中
# ac.move_to_element(ele)
# #调用perform()来执行鼠标操作
# ac.perform()
#
ActionChains(driver).move_to_element(ele).perform()

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="高级搜索"]')))
driver.find_element_by_xpath('//a[text()="高级搜索"]').click()

