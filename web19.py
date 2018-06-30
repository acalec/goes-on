"""
2016/11/30

web 19


1, 标准化的程序模板

2, 网络安全

3, 写简历、投简历和面试
    写简历 就是要吹
    投简历 海投 不要带任何感情
        100 起步
        200 不嫌多
        300 400 最好
        重复投
    面试
        什么都能答应
        只许我拒人 不可人拒我
"""

import requests

r = requests.post('http://127.0.0.1:3000/user/add', data={
    'username': 'gua1111',
    'xfrs': '066e3ec5-c50d-44e8-b04d-a8da45bd87ae',
})

print(r, r.text)