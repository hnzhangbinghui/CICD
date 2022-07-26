from time import sleep
import pytest
from selenium import webdriver
url = 'http://192.168.99.158:9080/acp-custody/login.html'


def test_login():
    driver = webdriver.Firefox()
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
    sleep(3)
    #断言登录成功
    assert 'cy' in driver.page_source

    sleep(3)
    driver.quit()




if __name__ == '__main__':
    pytest.main(["-vs", "login.py"])
