"""
with示例
打开一个文件  啦啦啦 
"""
# 方案一
f = open('xxx')

with open('file') as f:    # f = open('file')
    data = f.read()
    print(data)

# with语句块结束 则f自动销毁
