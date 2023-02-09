import time

import click
from atlassian import Jira
from gen_tdl import gen_tdl

started = time.strftime("%Y-%m-%d", time.localtime())
time_spend_in_seconds = 8 * 60 * 60


# 获取jira用户key
def get_jira_worker(jira, username):
    res = jira.user(username)
    return res.get('key')


# 获取jira用户姓名
def get_jira_username(jira, username):
    res = jira.user(username)
    return res.get('displayName').split('_')[1]


def get_issue_id(jira, issue_name):
    JQL = f'text ~ "{issue_name}"'
    data = jira.jql(JQL)
    # issue_id = data[0].get("id")
    issues = data.get('issues')
    issue = issues[0]
    return issue.get('id')


@click.command()
@click.option('--username', default='username', help='用户名，必填项')
@click.option('--password', default='Hello1234', help='密码（默认为Hello1234）')
@click.option('--url', default='http://work.agilestar.cn', help='URL（默认为http://work.agilestar.cn）')
@click.option('--started', default=started, help='填写时间（默认为当天日期，格式【2023-01-01】）')
@click.option('--time_spend_in_seconds', default=time_spend_in_seconds, help='工时（单位【秒】，默认为8小时）')
@click.option('--issue_name', default="业务工作台-23年优化需求", help='问题（默认业务工作台-23年优化需求）')
@click.option('--content', default="市场工作台开发", help='工作内容，必填项')
@click.option('--template', default="0", help='是否生成TDL模板（0：不生成，1：生成）')
def fill_tempo(username, password, url, started, time_spend_in_seconds, issue_name, content, template):
    jira = Jira(
        url=url,
        username=username,
        password=password)
    worker = get_jira_worker(jira, username)
    issue_id = int(get_issue_id(jira, issue_name))

    res = jira.tempo_timesheets_write_worklog(worker, started, time_spend_in_seconds, issue_id, content)
    print(f"填报完毕，填报放回报文：{res}")
    if template == "1":
        name = get_jira_username(jira, username)
        date = time.strftime('%-m{}%-d{}', time.strptime(started, "%Y-%m-%d")).format("月", "日")
        gen_tdl(name, date, content)


if __name__ == '__main__':
    fill_tempo()