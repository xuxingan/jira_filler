import openai

content = "1.在线协同表格公式无法保存bug处理2.宣传物料-基础数据配置开发（20%）"
title = content + '''
请帮我把以上的工作内容填充为今日总结,用以下形式输出:
1.进步的点
2.待改进的点
3.当日心得感悟
'''
openai.api_key = 'sk-10UlpKiOrCxXmtPfcegusT3BlbkFJhDNJxmKMnSz3IMEILNOh'
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
