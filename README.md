# jira_filler
填报jira工时的命令行小工具

## 使用方式：
1. 安装依赖`pip install -r requirements.txt`
2. `python fill_work_time.py --help`查看帮助文档
    ```bash 
   Options:
     --username TEXT                 用户名，必填项
     --password TEXT                 密码（默认为Hello1234）
     --url TEXT                      URL（默认为http://work.agilestar.cn）
     --started TEXT                  填写时间（默认为当天日期，格式【2023-01-01】）
     --time_spend_in_seconds INTEGER
                                     工时（单位【秒】，默认为8小时）
     --issue_name TEXT               问题（默认业务工作台-23年优化需求）
     --content TEXT                  工作内容，必填项(支持多条记录，用【1.2.3.】分开，最多支持三条工作内容)
     --template TEXT                 是否生成TDL模板（0：不生成，1：生成）
     --help                          Show this message and exit.
    ```
3. 命令行示例：`python fill_work_time.py --username=test --content=供应商管理开发（100%） --template=1
`