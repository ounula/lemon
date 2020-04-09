# -*- encoding:utf-8 -*-
# @Time : 2020/4/8 12:36 
# @Author : ZHH
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(service_log_path="E:\\chromedriver.log")
driver.get("http://www.baidu.com")
# 隐式等待
# driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("柠檬班")
driver.find_element_by_id("su").click()
#获得窗口句柄
handles=driver.window_handles
print(handles)
#等到元素可见
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//a[contains(text(),"吧_百度")]')))
driver.find_element_by_xpath('//a[contains(text(),"吧_百度")]').click()
#等待新窗口出现
WebDriverWait(driver,10).until(EC.new_window_is_opened(handles))
handles=driver.window_handles
print(handles)
# WebDriverWait(driver,10).until(EC.vel)
#窗口切换
driver.switch_to.window(handles[0])
driver.switch_to.window(handles[1])
print(driver.current_window_handle)
#alert 切换
alert=driver.switch_to.alert
#接受
alert.accept()
#取消
alert.dismiss()
#获取alert内容
print(alert.text)