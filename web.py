import os
import time

import pywebio
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *

from fill_work_time import fill_tempo_inner

pywebio.config(title='Jira填报', theme='sketchy')
password = 'Hello1234'
url = 'http://work.agilestar.cn'
started = time.strftime("%Y-%m-%d", time.localtime())
time_spend_in_seconds = 8 * 60 * 60
issue_name = '业务工作台-23年优化需求'
template = "1"
path = os.path.dirname(__file__) + '/tdl/'
date = time.strftime('%-m{}%-d{}', time.strptime(started, "%Y-%m-%d")).format("月", "日")


def main():
    put_markdown("""# Jira填报

    [`Jira`](http://work.agilestar.cn/secure/Dashboard.jspa)填报用于填写Jira的Tempo插件中的每日工作日志，并生成TDL模板用于回填`工作台TDL`腾讯在线文档。
    基于ChatGPT-3模型的`每日总结`生成功能预计下版本支持。

    本程序的源代码[链接](https://github.com/xuxingan/jira_filler)
    """)

    info = input_group('今日的工作重点：', [
        input("用户名", name="username", type=TEXT),
        input("任务1.", name="content1", type=TEXT),
        input("任务2.", name="content2", type=TEXT),
        input("任务3.", name="content3", type=TEXT),
    ])
    username = info['username']
    content1 = info['content1']
    content2 = info['content2']
    content3 = info['content3']
    content = f'1.{content1}2.{content2}3.{content3}'
    fill_tempo_inner(username, password, url, started, time_spend_in_seconds, issue_name, content, template)

    put_markdown(f"""
    ### 模板生成完毕
    """)

    c = open(os.path.join(path, f'{username}_{date}.xlsx'), 'rb').read()
    put_file(f'{username}_{date}.xlsx', c, f'{username}_{date}.xlsx')


if __name__ == '__main__':
    start_server(main, debug=True, port=666)
