# -*- encoding:utf-8 -*-
# @Time : 2020/4/9 11:00 
# @Author : ZHH
from selenium import webdriver
from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
#导入select 库
from selenium.webdriver.support.ui import Select
#导入鼠标操作库
from  selenium.webdriver.common.action_chains import ActionChains
#导入键盘操作库
from selenium.webdriver.common.keys import Keys
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

se_ele=driver.find_element_by_xpath('//select[@name="ft"]')
sele=Select(se_ele)
#通过文字
sele.select_by_visible_text('微软 Word (.doc)')
#通过value值
sele.select_by_value('rtf')
#通过下标
sele.select_by_index('4')
'''
键盘操作需要搭配send_keys()使用
如
send_keys(Keys.CONTROL,'a') 全选
常用
回车  Keys.ENTER
删除键 Keys.BACK_SPACE
空格键 Kes.SPACE
制表键 Kes.TAB
回退键 Kes.ESCAPE
刷新     Kes.F5
'''

