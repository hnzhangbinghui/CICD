from time import sleep
import pytest
from selenium import webdriver
url = 'http://192.168.99.158:9080/acp-custody/login.html'
from datetime import datetime


def test_login():
    driver = webdriver.Edge(r"C:\Program Files (x86)\Microsoft\Edge\Application\new_msedge.exe")
    driver.get(url)
    #隐形等待
    driver.implicitly_wait(20)
    driver.maximize_window()
    sleep(3)
    # 输入用户名
    account = driver.find_element_by_xpath("//input[@id='pwdUserName']")
    account.clear()
    account.click()
    account.send_keys('cy')
    sleep(1)
    # 输入密码
    passwd=driver.find_element_by_xpath("//input[@id='pwdPassword']")
    passwd.clear()
    passwd.click()
    passwd.send_keys("Ysstech123!@#")
    sleep(1)
    #点击登录按钮
    driver.find_element_by_xpath("//button[@id='login-btn']").click()
    driver.implicitly_wait(10)
    sleep(3)
    driver.get_screenshot_as_file(r"C:\Users\zhangbinghui\PycharmProjects\CICDAUTO\img\\aaa.png")
    #断言登录成功
    assert 'cy' in driver.page_source
    # img_path="C:\Users\zhangbinghui\PycharmProjects\CICDAUTO\img"+datetime.now()





    sleep(5)
    driver.quit()




if __name__ == '__main__':
    pytest.main(["-vs", "login.py"])
