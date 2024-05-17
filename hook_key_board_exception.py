import sys
import os
import traceback

def excepthook_decorator(excepthook):
    def reformat(frame, format):
        format[0] = 'Traceback (most recent call last):\n' + format[0]
        row = []
        row.append('  File "{}", line {}, in {}\n'.format(
            frame['filename'], frame['lineno'], frame['name']))
        if frame['line']:
            row.append('    {}\n'.format(frame['line'].strip()))
        if frame['locals']:
            for name, value in sorted(frame['locals'].items()):
                row.append('    {name} = {value}\n'.format(name=name, value=value))
        if frame['exname']:
            row.append(frame['exname'])
        result = ''.join(row)
        format[-1] = result
        return format
    def wrapper(exctype, value, exctracback):
        if exctype is KeyboardInterrupt:
            # 假设的包路径和文件名
            package_path = "/root/anaconda3/lib/python3.9/site-packages/"
            frame = {
                'filename': os.path.join(package_path, 'mindx', '__init__.py'), 
                'lineno': 57, 
                'name': 'write', 
                'line': 'time.sleep(6)', 
                'locals': None, 
                'exname': 'KeyboardInterrupt'
            }
            format = traceback.format_tb(exctracback)
            msg = ''.join(reformat(frame, format))
            # add the jepg image 
            package_path = "/home/demo/"
            frame = {
                'filename': os.path.join(package_path, 'main.py'), 
                'lineno': 21, 
                'name': '<module>', 
                'line': 'ret.write("/home/demo/output.jepg")', 
                'locals': None, 
                'exname': 'KeyboardInterrupt'
            }
            format = traceback.format_tb(exctracback)
            __msg = ''.join(reformat(frame, format))
            __msg = __msg.replace("KeyboardInterrupt", "")

            # print(f"__msg", __msg)
            # print(f"msg", msg)
            msg = "Traceback (most recent call last):\n" + __msg + msg

            print(msg, file=sys.stderr)
            # print("Traceback (most recent call last):", end="")

        else:
            excepthook(exctype, value, exctracback)
    return wrapper


def hook_keyboard_excetion_hw():

    # 设置自定义的异常处理函数
    sys.excepthook = excepthook_decorator(sys.excepthook)

if __name__ == "__main__":
    hook_keyboard_excetion_hw()
    # 测试代码，主动引发 KeyboardInterrupt 异常
    raise KeyboardInterrupt
