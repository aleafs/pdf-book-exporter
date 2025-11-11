#!/usr/bin/env python3

import os

class Config:
    title: str
    vendor: str
    prefix: str
    logo: str

    def __init__(self, path: str):
        self.title='Bluepipe'
        self.vendor='杭州萃蓝网络科技有限公司'
        self.prefix='bluepipe'
        self.logo=''

        if os.path.isdir(path):
            for name in os.listdir(path):
                print(name)

if __name__ == '__main__':
    config = Config('/product')
    print(config.title)
