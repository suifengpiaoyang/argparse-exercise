"""
让我们升级任务的难度，让它更具挑战性。这次的任务是创建一个日志分析器命令行工具，它接受一个日志文件作为输入，并提供一些有关日志的统计信息。

任务要求如下：

    创建一个名为log_analyzer.py的Python脚本。
    使用argparse库解析命令行参数。
    接受一个日志文件作为位置参数，并将其路径存储在变量中。
    提供一个可选参数--level，用于过滤指定日志级别的日志条目（如DEBUG、INFO、ERROR等）。
    提供一个可选参数--count，用于指定要显示的日志条目数量。
    分析日志文件，并根据过滤条件和数量限制输出相应的日志条目。

下面是一个示例输入和输出的演示：

$ python log_analyzer.py log.txt --level ERROR --count 10
===== Log Analyzer =====
Log File: log.txt
Filter Level: ERROR
Number of Entries: 10

[2023-05-30 12:45:23] ERROR: Something went wrong
[2023-05-30 13:15:41] ERROR: Another error occurred
...
"""
import argparse
import os
import re
import sys


parser = argparse.ArgumentParser(description='a tool to print log easily')

parser.add_argument('file', help='the log file absolute path')
parser.add_argument('-l', '--level', help='specify log level')
parser.add_argument('-c', '--count', help='specify the print log numbers')

args = parser.parse_args()

path = os.path.abspath(args.file)
if not os.path.exists(path):
    print(f'File [{path}] not found!')
    sys.exit()

with open(path, encoding='utf-8')as fl:
    if args.level:
        level = args.level.upper()
        logs = re.findall(rf'\[.*?\]\s{level}\:.*?\n', fl.read())
    else:
        level = ''
        logs = fl.readlines()
if args.count:
    logs = logs[:int(args.count)]

output = f'''===== Log Analyzer =====
Log File: {args.file}
Filter Level: {level}
Number of Entries: {len(logs)}
'''
# print(args)
print(output + '\n' + ''.join(logs))
