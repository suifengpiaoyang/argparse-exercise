"""
以下是根据您的建议重新设计的任务：

创建一个命令行工具，用于计算和显示数学公式的结果。该工具将支持不同的数学运算，并接受参数来执行这些运算。

要求如下：

    创建一个名为math_calculator.py的 Python 脚本。
    使用argparse库解析命令行参数。
    支持以下数学运算：
        add: 执行加法运算，接受两个数字作为参数，并返回它们的和。
        subtract: 执行减法运算，接受两个数字作为参数，并返回它们的差。
        multiply: 执行乘法运算，接受两个数字作为参数，并返回它们的积。
        divide: 执行除法运算，接受两个数字作为参数，并返回它们的商。
    数字参数作为位置参数提供，可以输入任意数量的数字。
    每个数学运算都应在命令行中显示适当的输出结果。

以下是一个示例输入和输出的演示：

$ python math_calculator.py add 5 3
Result: 8

$ python math_calculator.py subtract 10 4
Result: 6

$ python math_calculator.py multiply 6 7
Result: 42

$ python math_calculator.py divide 20 5
Result: 4.0
"""
import argparse


parser = argparse.ArgumentParser(
    description='calc two numbers',
    epilog='Use "<sub-command> -h" to see sub command help'
)
subparsers = parser.add_subparsers(help='sub-commands help',
                                   dest='command')
add = subparsers.add_parser('add', help='add numbers')
add.add_argument('numbers', nargs=2)
subtract = subparsers.add_parser('subtract', help='subtract numbers')
subtract.add_argument('numbers', nargs=2)
multiply = subparsers.add_parser('multiply', help='multiply numbers')
multiply.add_argument('numbers', nargs=2)
divide = subparsers.add_parser('divide', help='divide numbers')
divide.add_argument('numbers', nargs=2)
args = parser.parse_args()

command = args.command
numbers = args.numbers
num1 = int(numbers[0])
num2 = int(numbers[1])
if command == 'add':
    print(num1 + num2)
elif command == 'subtract':
    print(num1 - num2)
elif command == 'multiply':
    print(num1 * num2)
elif command == 'divide':
    print(num1 / num2)
