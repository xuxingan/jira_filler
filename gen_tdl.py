import os

from xlsxtpl.writerx import BookWriter


def gen_tdl(name, date, content):
    path = os.path.dirname(__file__) + '/tdl/'
    file_name = os.path.join(path, 'tdl.xlsx')
    writer = BookWriter(file_name)
    writer.jinja_env.globals.update(dir=dir, getattr=getattr)

    payloads = []
    lo_info = {'name': name, 'date': date, 'content': content}
    payloads.append(lo_info)
    writer.render_book(payloads=payloads)
    file_name = os.path.join(path, f'{date}.xlsx')
    writer.save(file_name)
    print(f"TDL文件生成完毕，文件位置{file_name}")


if __name__ == "__main__":
    gen_tdl('test', '2月7日', '供应商管理（100%）')
