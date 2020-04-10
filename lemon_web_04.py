from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import win32con
import win32gui
#谷歌浏览器
def upload_file(filepath):
    # driver=webdriver.Chrome()
    # driver.get("http://pan.baidu.com")
    dialog=win32gui.FindWindow("#32770","打开")#一级窗口
    comboxex32=win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)#二级
    comobox=win32gui.FindWindowEx(comboxex32,0,"ComboBox",None)#三级
    eidit=win32gui.FindWindowEx(comobox,0,"Edit",None)#四级
    button=win32gui.FindWindowEx(dialog,0,"Button","打开(&O)")#button
    #操作
    win32gui.SendMessage(eidit,win32con.WM_SETTEXT,None,filepath)
    win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)

if __name__ == '__main__':
    upload_file('D:\\新建文本文档.txt')