import json
import random

import openai
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *


def read_json():
    with open('story/data.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def gpt(title):
    openai.api_key = ''
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": title}]
    )

    text1 = completion["choices"][0]["message"]["content"]
    print(text1)
    return text1


def gen_story(name, dept, theme, num):
    content = f"模仿以下文章生成一篇新文章，人物换成'{name}'，部门换成'{dept}'，主题换成'{theme}'，字数控制在{num}字"
    random_story = read_json()
    # 从json中随机取一篇文章
    random_story = random_story[random.randint(0, 60)]['content']
    title = content + random_story
    return gpt(title)


def story():
    put_markdown("""# 你比安徒生都会讲故事
    基于GPT-3.5模型生成企业文化小故事
    本程序的源代码[链接](https://github.com/xuxingan/jira_filler)
    """)
    img = open('story/andersen.jpg', 'rb').read()
    put_image(img, width='30%')
    info = input_group('故事信息填写：', [
        input("主人公", name="uname", type=TEXT),
        input("部门", name="dept", type=TEXT),
        input("主题", name="theme", type=TEXT),
        input("字数", name="num", type=TEXT)
    ])
    name = info['uname']
    dept = info['dept']
    theme = info['theme']
    num = info['num']
    # 判断num为空就默认300字
    if num == '':
        num = 300
    put_markdown(f"""
      #### 由于调用了OpenAI接口，速度很慢，公共key限制使用次数，不要轻易刷新，故事编造中。。。
      """)
    story = gen_story(name, dept, theme, num)

    put_markdown(f"""
    ### 故事生成完毕
    """)
    put_markdown(f" {story}")


if __name__ == '__main__':
    start_server(story, debug=True, port=777)
