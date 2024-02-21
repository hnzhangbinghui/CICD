from selenium import webdriver


class ChromeOptions():
    def options(self):
        # chrome浏览器的配置项，可以通过修改默认参数，改变默认启动的浏览器状态；
        options = webdriver.ChromeOptions()
        # 将浏览器默认设置为最大窗体（启动浏览器，立即最大化，速度稳定性机器高效）
        # options.add_argument('start-maxminzed')
        # 设置默认窗体的启动大小
        options.add_argument('window-size=400,2000')
        # 无头模式，虽然看不到，但是一切照旧，在一些特定场景下会失败
        options.add_argument('--headless')
        # 去掉默认的提示自动化信息（没啥用），一般没什么影响。警告条可能会导致页面内容遮挡或挤压，影响自动化测试
        options.add_argument('excludeSwitches', ['enable-automation', 'enable-logging'])
        # 去掉控制台多余信息
        options.add_argument('excludeSwitches', ['enable-logging'])
        # 老版本去掉警告条的参数，已经不生效了。已弃用
        options.add_argument('disable-infobars')
        # 读取本地缓存，实现一个有缓存的浏览器，这个指令执行前必须关闭所有本地的chrome浏览器
        options.add_argument(r'C:\Users\zhangbinghui\AppData\Local\Google\Chrome\User Data')
        # 去掉账号密码弹框
        perfs={}
        perfs['credentials-enable-service'] = False
        perfs['profile.password_manager_enable'] = False
        options.add_experimental_option("prefs", perfs)
        # 指定窗口打开的位置
        options.add_argument('window-position=2200,500')
        # 隐身模式
        options.add_argument('incognito')
        return options




