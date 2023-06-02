# 文件重命名命令行工具

## 使用帮助

```
$ python file_renamer.py -h
usage: file_renamer.py [-h] [-s SEARCH] [-r PATTERN REPLACE_TEXT] [--regex]
                       [-a ADD_PREFIX] [-b ADD_SUFFIX] [--dry-run]
                       path [path ...]

raname files in one or multi folder

positional arguments:
  path                  the folder path, it can be one or multi folder, use
                        space to seperate them.

optional arguments:
  -h, --help            show this help message and exit
  -s SEARCH, --search SEARCH
                        search mode, this parameter must be specified.
  -r PATTERN REPLACE_TEXT, --replace PATTERN REPLACE_TEXT
                        Replace mode, you must input two values, first is
                        match pattern, second is replace text. You can use
                        --regex to use regex
  --regex               Use regular expression pattern, the default match
                        pattern is wildcard. This parameter will affect -s
                        and -r
  -a ADD_PREFIX, --add-prefix ADD_PREFIX
                        add prefix for files
  -b ADD_SUFFIX, --add-suffix ADD_SUFFIX
                        add subffix for files, using the last point for
                        seperate.
  --dry-run             perform a dry run without actually renaming files.
                        The matched files will be listed, but no renaming
                        will occur.
```

## 说明

- 在实际操作前使用 --dry-run 来看结果是不是符合预期再去掉 --dry-run 实际运行。
- 可以通过使用 --regex 将所有的 pattern 换成正则表达式的输入来获取更加精准的匹配。
- 默认使用通配符匹配。

## 使用示例

### 给所有 txt 文件增加前缀 test

```
python file_renamer.py -s *.txt -a test
```

后缀的增加同理

### 将所有 .jpg 文件的后缀替换成 png

```
python file_renamer.py -s *.jpg -r jpg png
```





