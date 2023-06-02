"""
当然！我很乐意再为您布置一个稍微更具挑战性的任务，旨在进一步提高您对 argparse 的熟练程度。

创建一个命令行工具，用于批量重命名文件。该工具将提供以下功能：

    支持指定一个或多个文件夹路径，并按照指定规则重命名文件。
    支持指定文件名的搜索模式，并仅对匹配的文件进行重命名。
    支持使用通配符模式或正则表达式模式进行文件名匹配。
    支持指定重命名规则，包括替换、添加前缀或后缀等操作。

要求：

    创建一个名为 file_renamer.py 的 Python 脚本。
    使用 argparse 库解析命令行参数。
    支持以下参数和选项：
        path：要重命名文件的一个或多个文件夹路径。可以指定多个路径进行批量重命名。
        -s/--search：文件名的搜索模式。只有匹配此模式的文件才会被重命名。
        -r/--replace：替换模式。指定一个字符串，将匹配到的文件名中的一部分替换为该字符串。
        -a/--add-prefix：添加前缀。指定一个字符串，在匹配到的文件名前添加该前缀。
        -b/--add-suffix：添加后缀。指定一个字符串，在匹配到的文件名后添加该后缀。
        --dry-run：演示模式。执行命令时不实际重命名文件，而是显示重命名的结果。
        --regex：使用正则表达式模式进行文件名匹配。默认使用通配符模式。
    如果指定了搜索模式，将只对匹配到的文件进行重命名操作。
    如果指定了替换、添加前缀或添加后缀中的任何一个或多个选项，则将根据指定的规则对文件进行重命名。
    如果使用了 --dry-run 演示模式，则不实际重命名文件，而是显示重命名的结果。

通过增加 --regex 选项，用户可以显式指定使用正则表达式模式进行文件名匹配，而默认情况下将使用通配符模式。

以下是一个示例输入和输出的演示：

$ python file_renamer.py -p folder -s "*.txt" -r "_new" --dry-run
Renaming files in folder: folder

Matched files:
1. file1.txt -> file1_new.txt
2. file2.txt -> file2_new.txt
3. file3.txt -> file3_new.txt

Dry run completed. No files were actually renamed.

$ python file_renamer.py -p folder -s "file.*" -a "prefix_" -b "_suffix"
Renaming files in folder: folder

Renamed files:
1. file1.txt -> prefix_file1_suffix.txt
2. file2.txt -> prefix_file2_suffix.txt
3. file3.txt -> prefix_file3_suffix.txt

Renaming completed. Total 3 files were renamed.
"""
import argparse
import fnmatch
import os
import re
import shutil
import sys

from copy import deepcopy

parser = argparse.ArgumentParser(
    description='raname files in one or multi folder'
)
parser.add_argument('path',
                    nargs='+',
                    help='the folder path, it can be one or multi folder, '
                    'use space to seperate them.')
parser.add_argument('-s',
                    '--search',
                    help='search mode, this parameter must be specified.')
parser.add_argument('-r',
                    '--replace',
                    nargs=2,
                    metavar=('PATTERN', 'REPLACE_TEXT'),
                    help='Replace mode, you must input two values, '
                    'first is match pattern, second is replace text. '
                    'You can use --regex to use regex')
parser.add_argument('--regex',
                    action='store_true',
                    help='Use regular expression pattern, the '
                    'default match pattern is wildcard. This '
                         'parameter will affect -s and -r')
parser.add_argument('-a',
                    '--add-prefix',
                    help='add prefix for files')
parser.add_argument('-b',
                    '--add-suffix',
                    help='add subffix for files, using the last point '
                    'for seperate.')
parser.add_argument('--dry-run',
                    action='store_true',
                    help='perform a dry run without actually renaming files. '
                    'The matched files will be listed, '
                    'but no renaming will occur.')
args = parser.parse_args()

if not args.search:
    print('Please use -s or --search to specify the search mode.')
    sys.exit()

pattern = args.search
dry_run = args.dry_run
if args.regex:
    match_mode = 'regex'
else:
    match_mode = 'wildcard'
for folder in args.path:
    path = os.path.abspath(folder)
    index = 1
    print(f'Renaming files in folder: {folder}\n')
    if not os.path.exists(path):
        print(f'Error: path [{path}] not found!\n')
        continue
    print('Matched files:')
    for file in os.listdir(path):
        new_file = deepcopy(file)
        filepath = os.path.join(path, file)
        if not os.path.isfile(filepath):
            continue
        if match_mode == 'wildcard':
            flag = fnmatch.fnmatch(file, pattern)
        elif match_mode == 'regex':
            flag = re.findall(rf'{pattern}', file)
        if not flag:
            continue
        if args.add_prefix:
            new_file = args.add_prefix + new_file
        if args.add_suffix:
            if '.' in new_file:
                head, tail = new_file.rsplit('.', 1)
                new_file = head + args.add_suffix + '.' + tail
            else:
                new_file += args.add_suffix
        if args.replace:
            if match_mode == 'wildcard':
                new_file = new_file.replace(*args.replace)
            elif match_mode == 'regex':
                rpattern, repl = args.replace
                new_file = re.sub(rf'{rpattern}', repl, new_file)
        if new_file == file:
            print(f'{index}. {file}')
        else:
            print(f'{index}. {file} -> {new_file}')
        if not dry_run:
            new_filepath = os.path.join(path, new_file)
            shutil.move(filepath, new_filepath)
        index += 1
if dry_run:
    print('\nDry run completed. No files were actually renamed.')
else:
    print('\nTask done!')
