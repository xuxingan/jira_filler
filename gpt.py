import openai

content = "1.测试环境工作流流程图问题处理2.宣传物料基础数据管理开发(40%)"
title = content + '''
请帮我把以上的工作内容填充为今日总结,用以下形式输出:
1.进步的点
2.待改进的点
3.当日心得感悟
'''
# openai.api_key = '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'
# # 文本类
# response = openai.Completion.create(
#     model='text-davinci-003',
#     prompt=title,
#     temperature=0.7,
#     top_p=1.0,
#     max_tokens=512,
#     frequency_penalty=0.0,
#     presence_penalty=0.0,
#     n=1
# )
# text1 = response.choices[0].text
# print(text1)
#

testdemo = '''
进步的点：
今日我完成了测试环境工作流流程图的问题处理，宣传物料基础数据管理开发，掌握了系统的基本功能，并且能够快速解决问题，提高了自己的效率。

待改进的点：
宣传物料基础数据管理开发的部分，还需要不断改进，以提高系统的安全性，并且还需要更多的测试，以确保系统的可靠性。

当日心得感悟：
今日的工作任务非常艰苦，但是我也从中学到了很多，比如如何解决问题，如何提高自己的效率，以及如何改进系统的安全性等等。这些经验和知识都是对我未来工作有很大帮助的。
'''

lines = testdemo.split("\n")  # 先将文本按照换行符分割成多行（如果有换行符的话）

for line in lines:
    if "：" in line:  # 如果当前行包含冒号
        index = line.index("：")  # 获取冒号的位置
        content = line[index + 1:].strip()  # 获取冒号后面的内容，并去除两侧的空格
        print(content)  # 输出冒号后面的内容
