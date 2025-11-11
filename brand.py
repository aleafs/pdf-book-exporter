#!/usr/bin/env python3

import os
import yaml

class Config:
    title = 'Bluepipe'
    prefix = 'bluepipe'
    vendor = '杭州萃蓝网络科技有限公司'
    logo = None

    def __init__(self, path: str):
        with open(os.path.join(path, 'config.yaml'), 'r', encoding='utf-8') as f:
            meta = yaml.safe_load(f.read())
            print(meta)

        if os.path.isdir(path):
            for name in os.listdir(path):
                print(name)
                if name.startswith('logo.'):
                    self.logo = os.path.join(path, name)

if __name__ == '__main__':
    config = Config('/product')
    print(config.title)
