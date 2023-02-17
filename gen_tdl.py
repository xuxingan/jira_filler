import os
import re

from xlsxtpl.writerx import BookWriter


def gen_tdl(username, name, date, content):
    path = os.path.dirname(__file__) + '/tdl/'
    file_name = os.path.join(path, 'tdl.xlsx')
    writer = BookWriter(file_name)
    writer.jinja_env.globals.update(dir=dir, getattr=getattr)

    payloads = []
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
    lo_info = {'name': name, 'date': date, 'content1': content1, 'content2': content2, 'content3': content3}

    payloads.append(lo_info)
    writer.render_book(payloads=payloads)
    file_name = os.path.join(path, f'{username}_{date}.xlsx')
    writer.save(file_name)
    print(f"TDL文件生成完毕，文件位置{file_name}")


if __name__ == "__main__":
    gen_tdl('test', '2月7日', '供应商管理（100%）')
