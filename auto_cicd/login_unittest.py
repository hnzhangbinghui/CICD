from datetime import datetime
from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

url = 'http://192.168.99.158:9080/acp-custody/login.html'


class Test(unittest.TestCase):
    def test_login(self):
        print("打开浏览器")
        driver = webdriver.Edge(r"D:\Anaconda3\Scripts\MicrosoftWebDriver.exe")
        # driver = webdriver.Firefox()
        # driver=webdriver.Firefox()
        driver.get(url)
        # 隐形等待
        driver.implicitly_wait(20)
        driver.maximize_window()
        sleep(3)
        # 获取当前页面title
        print(driver.title)
        # 获取当前url
        print(driver.current_url)
        # 输入用户名
        account = driver.find_element(by=By.XPATH, value="//input[@id='pwdUserName']")
        # find_element_by_xpath("//input[@id='pwdUserName']")
        account.clear()
        account.click()
        account.send_keys('cy')
        sleep(1)
        # 获取输入框的尺寸
        print(account.size)
        print("占位符", account.text)
        # 输入密码
        passwd = driver.find_element(by=By.XPATH, value="//input[@id='pwdPassword']")

        # find_element_by_xpath("//input[@id='pwdPassword']")
        passwd.clear()
        passwd.click()
        passwd.send_keys("Ysstech123!@#")
        sleep(1)
        # 点击登录按钮
        driver.find_element(by=By.XPATH, value="//button[@id='login-btn']").click()

        # find_element_by_xpath("//button[@id='login-btn']").click()
        driver.implicitly_wait(10)
        sleep(3)
        driver.get_screenshot_as_file(
            r"C:\Users\zhangbinghui\PycharmProjects\CICDAUTO\img\\aaa.png")
        # 断言登录成功
        assert 'cy' in driver.page_source
        # img_path="C:\Users\zhangbinghui\PycharmProjects\CICDAUTO\img"+datetime.now()
        sleep(5)
        driver.quit()
        print("关闭浏览器")


if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(Test("test_login"))
    runner=unittest.TextTestRunner()
    runner.run(suite)

