import openai
import re


def gen_summary(content):
    title = content + '''
    请帮我把以上的工作内容填充为今日总结,用以下形式输出:
    1.进步的点
    2.待改进的点
    3.当日心得感悟
    每一个细项内容不超过一行
    '''
    return gpt(title)


def gen_tomorrow(content):
    title = content + '''
    以上是我今天的工作内容，帮我根据今天内容生成一个明天工作计划，内容不超过三行，并且去掉百分比
    '''
    return gpt(title)


def gpt(title):
    openai.api_key = ''
    # 文本类
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=title,
        temperature=0.7,
        top_p=1.0,
        max_tokens=512,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        n=1
    )
    text1 = response.choices[0].text
    print(text1)

    pattern = r"\d+.(.+)"
    return re.findall(pattern, text1)


if __name__ == '__main__':
    # 总结
    content = "1.宣传物料测试反馈问题处理2.jenkins自动部署腾讯云前后端环境3.防火墙策略申请流程需求开发（20%）"
    print(gen_summary(content))

    # 明日工作内容
    # content = '''1.宣传物料测试反馈问题处理2.jenkins自动部署腾讯云前后端环境3.防火墙策略申请流程需求开发（20%）'''
    # print(gen_tomorrow(content))
