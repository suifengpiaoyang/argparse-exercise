"""
任务描述如下：

创建一个命令行工具，用于统计文本文件中的单词数量和行数。该工具将提供以下功能：

    支持统计单个文件的单词数量和行数。
    支持统计多个文件的单词数量和行数，并输出总计。
    可选择是否忽略空行和标点符号。

要求如下：

    创建一个名为word_counter.py的 Python 脚本。
    使用argparse库解析命令行参数。
    支持以下参数和选项：
        -f/--file：要统计的文件路径。可以接受单个文件路径或多个文件路径。
        -l/--lines：统计文件的行数。
        -w/--words：统计文件的单词数量。
        --ignore-empty-lines：忽略空行。
    如果提供了多个文件路径，将输出每个文件的统计结果，并在最后输出总计。

以下是一个示例输入和输出的演示：
$ python word_counter.py -f file1.txt -f file2.txt -l -w
file1.txt:
Lines: 10
Words: 100

file2.txt:
Lines: 15
Words: 150

Total:
Lines: 25
Words: 250

$ python word_counter.py -f file.txt -l -w --ignore-empty-lines
file.txt:
Lines: 10
Words: 90
"""
import argparse
import os
import re
import sys


parser = argparse.ArgumentParser(
    description='count the number of words and lines in files'
)

parser.add_argument(
    '-f',
    '--file',
    action='append',
    help='the input file path, can input one or multi path, ' +
    'this parameter must be specified.'
)
parser.add_argument('-l',
                    '--lines',
                    action='store_true',
                    help='count files lines')
parser.add_argument('-w',
                    '--words',
                    action='store_true',
                    help='count files words')
parser.add_argument('--ignore-empty-lines',
                    action='store_true',
                    help='ignore files empty lines')
args = parser.parse_args()

total = {'Lines': 0, 'Words': 0}
if not args.file:
    print('Parameter file must be specified!')
    sys.exit()
if not args.lines and not args.words:
    print('You must specify -l or -w parameter.')
    sys.exit()
for file in args.file:
    print(file + ':')
    path = os.path.abspath(file)
    if not os.path.exists(path):
        print(f'File [{path}] not found!')
    else:
        with open(path)as fl:
            data = fl.read()
        if args.ignore_empty_lines:
            data = re.sub(r'\n+', '\n', data)
    if args.lines:
        lines = len(re.findall(r'\n', data))
        total['Lines'] += lines
        print(f'Lines: {lines}')
    if args.words:
        words = len(re.findall(r'\b\S+\b', data))
        total['Words'] += words
        print(f'Words: {words}')
    print()

print('Total:')
if args.lines:
    print('Lines:', total['Lines'])
if args.words:
    print('Words:', total['Words'])
