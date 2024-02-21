from datetime import datetime
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options

url = 'http://192.168.99.158:9080/acp-custody/login.html'


def test_login():
    # 设置无头模式
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument("--disable-gpu")
    driver = webdriver.Firefox(options=options)  # 设置火狐为headless无界面模式

    # driver = webdriver.Edge(r"D:\Anaconda3\Scripts\MicrosoftWebDriver.exe")
    # driver = webdriver.Firefox()
    driver.get(url)
    # 隐形等待
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
    passwd = driver.find_element_by_xpath("//input[@id='pwdPassword']")
    passwd.clear()
    passwd.click()
    passwd.send_keys("Ysstech123!@#")
    sleep(1)
    # 点击登录按钮
    driver.find_element_by_xpath("//button[@id='login-btn']").click()
    driver.implicitly_wait(10)
    sleep(3)
    driver.get_screenshot_as_file(
        r"C:\Users\zhangbinghui\PycharmProjects\CICDAUTO\img\\aaa.png")
    # 断言登录成功
    assert 'cy' in driver.page_source
    # img_path="C:\Users\zhangbinghui\PycharmProjects\CICDAUTO\img"+datetime.now()

    sleep(5)
    driver.quit()


if __name__ == '__main__':
    pytest.main(["-vs", "login.py"])
