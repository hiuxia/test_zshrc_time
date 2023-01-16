import re
import subprocess
import time
from pathlib import Path


def get_execution_time(command):
    start_time = time.time()
    if type(command) == list:
        subprocess.run(command, shell=True,
                       executable='/opt/homebrew/bin/zsh')  # function exection
    elif type(command) == str:
        subprocess.run([command.strip("\n")],  shell=True,
                       executable='/opt/homebrew/bin/zsh')  # single command
    execution_time = (time.time() - start_time)*1e3
    return execution_time  # return milliseconds


zsh_config = Path("/Users/wanghaonan/.zshrc")
if zsh_config.is_file():
    with open(zsh_config, "r") as f:
        lines = f.readlines()
        function_list = []  # include multiple-line functions
        line_number = 0  # 第几条指令
        time_sum = 0
        for line in lines:
            # 判断不是空行，注释
            if line.strip("\t\n") and ('#' not in line):
                # the start of the function
                if re.compile("^.+()\s+{\s*\n?").match(line):
                    function_list.append(line)
                    continue
                elif re.compile("^}\s*\n").match(line):  # the end of the function
                    function_list.append(line.strip("\n"))
                    line_number += 1
                    # 执行函数
                    function_execution_time = get_execution_time(function_list)
                    time_sum += function_execution_time
                    print(
                        f"{line_number}: 命令：{''.join(function_list)}, 执行时间: {function_execution_time:.2f}ms")
                    function_list = []
                # the statement in the function
                elif re.compile("^(\t+|\s+)\w+").match(line):
                    function_list.append(line)
                else:
                    # line_number += 1
                    # 指令名称
                    if function_list == []:
                        line_number += 1
                        execution_time = get_execution_time(line)
                        time_sum += execution_time
                        print(
                            f"{line_number}: 命令：{line}, 执行时间: {execution_time:.2f}ms")
                    else:
                        function_list.append(line)

    print(f"{zsh_config} 执行共用时 {time_sum:.2f} ms")
