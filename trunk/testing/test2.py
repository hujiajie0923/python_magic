import time
import datetime
import re
import json
import requests
from requests.exceptions import RequestException
from multiprocessing import Pool
from bs4 import BeautifulSoup

GET = 'get'
POST = 'post'


class Crawler(object):

    def __init__(self, url=''):
        self.base_url = url

    def get_web_page(self, purpose=GET):
        headers = {
            # 默认谷歌浏览器请求头
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
        }
        # 请求体内容
        params = {
            'wd': 'python'
        }
        try:
            if purpose == GET:
                response = requests.get(self.base_url, headers=headers, params=params)
            else:
                response = requests.post(self.base_url, headers=headers, data=params)

            if response.status_code == 200:
                return response
                # response.text # 网页源码 [type: str]
                # response.headers # 头部信息 []
                # response.json() # json格式 [type: json]
                # response.content # 二进制数据 [type: bit]
                # response.cookies # 网页cookies [type: dict]
                # response.history # 访问的历史记录
            else:
                return None
        except RequestException:
            return None

    @staticmethod
    def parse_url(msg=''):
        regex = re.compile('[a-zA-Z]+://\S*')
        result = re.findall(regex, msg)
        print('find all url:\n', result)
        print('find all url down, total: {}'.format(len(result)))
        return result

    @staticmethod
    def main():
        source = crawler.get_web_page(purpose=GET)
        # 打印网页html内容
        print(source.text)


if __name__ == '__main__':
    crawler = Crawler(url='https://www.baidu.com')
    crawler.main()
