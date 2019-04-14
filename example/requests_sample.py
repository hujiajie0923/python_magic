# coding=UTF-8
import tkinter as tk
import requests
import re
import json
from requests.exceptions import RequestException
from fake_useragent import UserAgent


def display_info(func):
    def wrapper(*args, **kwargs):
        root = tk.Tk()
        root.title('Total URL:')

        text = tk.Text(root)
        text.grid(row=0, column=1)
        tk.Button(root, text='关闭', command=quit).grid(row=1, column=1)

        msg = func(*args, **kwargs)

        if msg:
            if isinstance(msg, (list, tuple)):
                for index, line in enumerate(msg):
                    text.insert(tk.END, 'line {}'.format(index+1) + ': \n' + str(line) + '\n\n')
            else:
                text.insert(tk.END, str(msg))

            # 让GUI始终处于居中位置
            root.update_idletasks()
            x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
            y = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
            root.geometry('+%d+%d' % (x, y))
            root.mainloop()
    return wrapper


def record_json_data(msg=None, do_read=False):
    if do_read:
        with open('crawler_data.json', 'r', encoding='utf-8') as wf:
            read_file = wf.read()
            file = json.loads(read_file)
            print('find json data:\n', file)
            print('find json data down, total: {}'.format(len(file)))
            return file
    with open('crawler_data.json', 'a', encoding='utf-8') as wf:
        wf.write(json.dumps(msg, ensure_ascii=False, indent=2) + '\n')


def get_web_page(url):
    # 使用随机请求头
    # ua = UserAgent(use_cache_server=False)
    # headers = {"User-Agent": ua.random}
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None


def parse_url(msg):
    regex = re.compile('[A-Za-z]+://\S*')
    result = re.findall(regex, msg)
    print('find all url:\n', result)
    print('find all url down, total: {}'.format(len(result)))
    return result


# @display_info
def main():
    url = 'http://www.baidu.com/'
    # 获取网页源代码
    result = get_web_page(url)
    if result:
        # 读取网页，筛选出URL
        url = parse_url(result)
        # 用json格式保存
        # record_json_data(msg=url)
        # 读取json文件
        # record_json_data(do_read=True)
    else:
        print('The URL is no such find')
    return url


if __name__ == '__main__':
    main()
