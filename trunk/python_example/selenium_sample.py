import time
import datetime
import re
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Browser(object):

    def __init__(self, url=''):
        self.url = url
        self.drive = webdriver.Chrome()
        self.waiting = None

    def switch_to_windows(self, to_parent_windows=False):
        """
        切换到不同的windows窗口
        :param to_parent_windows: 回到主窗口 if True
        :return:
        """
        total = self.drive.window_handles
        if to_parent_windows:
            self.drive.switch_to.window(total[0])
        else:
            current_windows = self.drive.current_window_handle
            for window in total:
                if window != current_windows:
                    self.drive.switch_to.window(window)

    def switch_to_frame(self, index=0, to_parent_frame=False, to_default_frame=False):
        """
        切换到不同的frame框架
        :param index: expect by frame index value or id or name or webelement
        :param to_parent_frame: 切换到上一个frame框架 if True
        :param to_default_frame: 切换到最上层的frame框架 if True
        :return:
        """
        if to_parent_frame:
            self.drive.switch_to.parent_frame()
        elif to_default_frame:
            self.drive.switch_to.default_content()
        else:
            self.drive.switch_to.frame(index)

    def open_new_windows(self, url=''):
        """
        打开一个新的windows窗口
        :param url: expect new url
        :return:
        """
        js = "window.open({})".format(url)
        self.drive.execute_script(js)
        time.sleep(2)

    def close_current_windows(self):
        if self.drive:
            self.drive.close()

    def quit_browser(self):
        if self.drive:
            self.drive.quit()

    def open_url(self):
        """
        Set the page timeout and execute the default URL
        :return:
        """
        # 显示等待10秒
        self.waiting = WebDriverWait(self.drive, 10)
        # 隐示等待10秒
        self.drive.implicitly_wait(10)
        # 打开url
        self.drive.get(self.url)

    def main(self):
        self.open_url()
        # 定位百度输入框
        # enter = self.drive.find_element_by_xpath('//*[@id="kw"]')
        enter = self.waiting.until(EC.presence_of_element_located(By.XPATH('//*[@id="kw"]')))
        # 模拟输入文本
        enter.send_keys('python')
        # 执行输入
        enter.send_keys(Keys.ENTER)
        # 得到网页html
        html = self.drive.page_source
        print('find html:\n', html)
        time.sleep(5)
        # 退出浏览器
        self.quit_browser()


if __name__ == '__main__':
    browser = Browser(url='http://baidu.com')
    browser.main()
