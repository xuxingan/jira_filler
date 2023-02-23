import os
import re

from xlsxtpl.writerx import BookWriter
from gpt import gen_tomorrow
from gpt import gen_summary


def gen_tdl(username, name, date, content):
    path = os.path.dirname(__file__) + '/tdl/'
    file_name = os.path.join(path, 'tdl.xlsx')
    writer = BookWriter(file_name)
    writer.jinja_env.globals.update(dir=dir, getattr=getattr)

    payloads = []
    # 生成今天工作内容
    content1 = ''
    content2 = ''
    content3 = ''
    matches = re.findall(r"\d+\..*?(?=\d+\.|$)", content)

    pattern = r"\d+\."

    if len(matches) == 3:
        content1 = re.sub(pattern, "", matches[0])
        content2 = re.sub(pattern, "", matches[1])
        content3 = re.sub(pattern, "", matches[2])
    elif len(matches) == 2:
        content1 = re.sub(pattern, "", matches[0])
        content2 = re.sub(pattern, "", matches[1])
    else:
        content1 = re.sub(pattern, "", matches[0])
    lo_info = {'name': name,
               'date': date,
               'content1': content1,
               'content2': content2,
               'content3': content3}

    # 生成明天工作内容
    tomorrows = gen_tomorrow(content)
    lo_info["tomorrow1"] = tomorrows[0]
    lo_info["tomorrow2"] = tomorrows[1]
    lo_info["tomorrow3"] = tomorrows[2]
    # 生成总结内容
    summarys = gen_summary(content)
    lo_info["summary1"] = summarys[0]
    lo_info["summary2"] = summarys[1]
    lo_info["summary3"] = summarys[2]
    payloads.append(lo_info)
    writer.render_book(payloads=payloads)
    file_name = os.path.join(path, f'{username}_{date}.xlsx')
    writer.save(file_name)
    print(f"TDL文件生成完毕，文件位置{file_name}")


if __name__ == "__main__":
    gen_tdl('test', '2月7日', '供应商管理（100%）')
