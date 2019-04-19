def mix_upper_lower(ptr: str, result_str: str):
    #  大小写混合字符串处理
    process_str = ptr
    lower_str = ''
    upper_str = ''
    local = 0
    length = len(process_str)
    while local < length:
        if 'a' <= ptr[local] <= 'z':
            process_str = ptr[local:]
            process_str_add = process_str + ' '
            for lower in process_str_add:
                if 'a' <= lower <= 'z':
                    lower_str += lower
                    local += 1
                else:
                    temp_str = lower_str + '         标识符\n'
                    result_str += temp_str
                    lower_str = ''
                    break
        else:
            process_str = ptr[local:]
            process_str_add = process_str + ' '
            for upper in process_str_add:
                if 'A' <= upper <= 'Z':
                    upper_str += upper
                    local += 1
                else:
                    temp_str = upper_str + '       非法输入符号\n'
                    result_str += temp_str
                    upper_str = ''
                    break
    return result_str


def lexical_analysis(analysis_str: str):
    analysis_str.replace('\r', ' ')
    wrap = analysis_str.find('\n')
    while wrap != -1:
        analysis_str = analysis_str.replace('\n', ' ')
        wrap = analysis_str.find('\n')
    analysis_str = analysis_str.lstrip()
    analysis_str = analysis_str.rstrip()
    analysis_str = analysis_str + ' '
    # analysis_str_copy = analysis_str
    to_be_process = []
    result_str = '词法分析结果：\n'
    # space = analysis_str.find(' ')
    to_be_process = analysis_str.split()
    for ptr in to_be_process:
        ptr_len = len(ptr)
        if ptr.isdigit():
            temp_str = ptr + '            数字\n'
            result_str += temp_str
        elif ptr.isalpha():
            if ptr.islower():
                if ptr == 'var':
                    temp_str = ptr + '          变量定义关键字\n'
                    result_str += temp_str
                else:
                    temp_str = ptr + '            标识符\n'
                    result_str += temp_str
            else:
                result_str = mix_upper_lower(ptr, result_str)
        elif ptr.isalnum():
            if '0' <= ptr[0] <= '9':
                temp_str += ptr + '               非法输入符号,标识符不能以数字开头\n'
                result_str += temp_str
        elif len(ptr) == 1:
            if ptr == ',':
                temp_str += ptr + '             标号,\n'
                result_str += temp_str
            elif ptr == ';':
                temp_str += ptr + '             标号;\n'
                result_str += temp_str
            elif ptr == '(':
                temp_str += ptr + '             标号(\n'
                result_str += temp_str
            elif ptr == ')':
                temp_str += ptr + '              标号)\n'
                result_str += temp_str
            elif ptr == '+':
                temp_str += ptr + '              标号+\n'
                result_str += temp_str
            elif ptr == ':':
                temp_str += ptr + '               标号:\n'
                result_str += temp_str
        elif len(ptr) >= 2:
            if ptr == ':=':
                temp_str += ptr + '               标号:= \n'
                result_str += temp_str
            else:
                local = 0
                pre_local = local
                # ptr_copy = ptr
                while local < ptr_len:
                    ptr = ptr + ' '
                    if 'a' <= ptr[local] <= 'z':
                        if ptr[local] != 'v' or ptr[local+1] != 'a' or ptr[local+2] != 'r':
                            local += 1
                            while 'a' <= ptr[local] <= 'z' or '0' <= ptr[local] <= '9':
                                local += 1
                            temp_str = ptr[pre_local:local] + '              标识符\n'
                            result_str += temp_str
                            pre_local = local
                        elif 'a' <= ptr[local+3] <= 'z' or '0' <= ptr[local+3] <= '9':
                            local += 4
                            while 'a' <= ptr[local] <= 'z' or '0' <= ptr[local] <= '9':
                                local += 1
                            temp_str = ptr[pre_local:local] + '            标识符\n'
                            result_str += temp_str
                            pre_local = local
                            # ptr_copy = ptr_copy[local:]
                        else:
                            temp_str = 'var' + '         关键字'
                            result_str += temp_str
                            local += 3
                            pre_local = local
                            # ptr_copy = ptr_copy[local:]
                    elif '1' <= ptr[local] <= '9':
                        local += 1
                        while '0' <= ptr[local] <= '9':
                            local += 1
                        if 'a' <= ptr[local] <= 'z':
                            temp_str = ptr[pre_local:local] + '         标识符不能以数字开头\n'
                            result_str += temp_str
                            pre_local = local
                        temp_str = ptr[pre_local:local] + '         数字\n'
                        result_str += temp_str
                        pre_local = local
                    elif ptr[local] == ',':
                        temp_str += ptr[pre_local:local] + '             标号,\n'
                        result_str += temp_str
                        local += 1
                        pre_local = local
                    elif ptr[local] == ';':
                        temp_str += ptr[pre_local:local] + '             标号;\n'
                        result_str += temp_str
                        local += 1
                        pre_local = local
                    elif ptr[local] == '(':
                        temp_str += ptr[pre_local:local] + '             标号(\n'
                        result_str += temp_str
                        local += 1
                        pre_local = local
                    elif ptr[local] == ')':
                        temp_str += ptr[pre_local:local] + '              标号)\n'
                        result_str += temp_str
                        local += 1
                        pre_local = local
                    elif ptr[local] == '+':
                        temp_str += ptr[pre_local:local] + '              标号+\n'
                        result_str += temp_str
                        local += 1
                        pre_local = local
                    elif ptr[local] == ':':
                        if ptr[local+1] == '=':
                            local += 2
                            temp_str += ptr[pre_local:local] + '               标号:=\n'
                            result_str += temp_str
                            pre_local = local
                        else:
                            temp_str += ptr[pre_local:local] + '               标号:\n'
                            result_str += temp_str
                            local += 1
                            pre_local = local
                    # elif ptr.isalnum():
                    #     if '0' <= ptr[0] <= '9':
                    #         temp_str += ptr + '               非法输入符号,标识符不能以数字开头\n'
                    #         result_str += temp_str
        else:
            temp_str += ptr + '                非法输入符号:\n'
            result_str += temp_str
    return result_str


if __name__ == "__main__":
    read_file = open("Source.txt", "r")
    write_file = open("result.txt", "w")
    write_file.write(lexical_analysis(read_file.read()))
    read_file.close()
    write_file.close()
    # str1 = input("请输入待分析的字符串:")
    # str2 = '  123  \n 123    123  adb abDaa ) ( ;'
    # print(lexical_analysis(str1))
    # print(lexical_analysis(str1))
    # str3 = lexical_analysis(str2)
    # print(str3)
    # print(str4)
