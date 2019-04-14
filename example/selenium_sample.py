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

    def switch_windows(self, index=0):
        """
        :param index: int
        """
        windows = self.drive.window_handles
        self.drive.switch_to.window(windows[index])

    def switch_frame(self, index=0, to_parent_frame=False, to_default_frame=False):
        """
        :param index: [by index or id or name or webelement] default: index=0
        :param to_parent_frame:
        :param to_default_frame:
        """
        if to_parent_frame:
            self.drive.switch_to.parent_frame()
        elif to_default_frame:
            self.drive.switch_to.default_content()
        else:
            self.drive.switch_to.frame(index)

    def open_new_window(self, url=''):
        js = "window.open({})".format(url)
        self.drive.execute_script(js)
        time.sleep(2)

    def open_url(self):
        self.drive.get(self.url)
        enter = self.drive.find_element_by_xpath('//*[@id="kw"]')
        enter.send_keys('python')
        enter.send_keys(Keys.ENTER)
        html = self.drive.page_source
        print(html)
        time.sleep(3)
        self.drive.quit()


if __name__ == '__main__':
    browser = Browser(url='http://baidu.com')
    browser.open_url()
