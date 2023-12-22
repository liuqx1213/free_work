import time

import requests
import re
import os
from typing import Tuple,Dict,List
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

if not os.path.isdir('get_pic'):
    os.mkdir('get_pic')
def get_response():
    try:
        for i in range(4, 10):
            your_url = 'https://pic.netbian.com/index_{}.html'.format(str(i))
            res = requests.get(url=your_url,headers=header)
            res.encoding = res.apparent_encoding
            src_path = re.compile('src="(/u.*?)" alt="(.*?)"')
            imgs = re.findall(src_path,res.text)
            get_data(imgs)
    except Exception as e:
        print("请求异常，异常结果为：{}".format(e))
    #print("your want:{}".format(imgs))


def get_data(imgs):
    for img in imgs:
        path = img[0]
        name = img[1].split(' ')[0]
        base_url = "https://pic.netbian.com"
        res_img = requests.get(url=base_url + path, headers=header)
        with open('./get_pic' + "/{}.jpg".format(name), 'wb') as f:
            f.write(res_img.content)
        print("{}******下载成功".format(name))

#静态类型的写法更加严谨
def func() -> List:
    #lst, lst2 = [7], [7]
    lst: List[int] = [7,8]
    lst2: List[int] = [7]
    lst3: List[int] = lst * 2
    #extend方法没有返回值，是给原列表的基础上增加了其他值
    #append方法也是没有返回值的，在添加时把需要添加的对象看做一个整体只会占用一个位置
    lst2.append(lst)
    #lst2.extend(lst)
    return lst3

def list_():
    a = 'Hello'
    b = a
    b = b.replace('l','r')
    print(b,a)


def greet(*args,**kwargs):
    for arg in args:
        if arg == 2:
            break
        print(arg,end=',\n')
    for key,value in kwargs.items():
        print(f'Key:{key},Value:{value}')


'''
map(func,list)函数可以接收一个函数和一个可迭代对象并且输出结果，常用配合就是lambda函数
filter(func,list)函数也可以节后一个可迭代对象并且输出过滤后的结果
'''

def pf():
    for a in range(10,1,-1):
        for b in range(1,a):
            print("*",end='')
        print()

if __name__ =='__main__':
    pf = pf()


