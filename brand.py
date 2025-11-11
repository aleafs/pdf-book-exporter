#!/usr/bin/env python3

import os
import pathlib
import sys

import yaml


def get_file_content(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()


class Config:
    title = 'Bluepipe'
    prefix = 'bluepipe'
    vendor = '杭州萃蓝网络科技有限公司'
    logo = None

    def __init__(self, path: str):

        root = pathlib.Path(os.path.join(os.path.dirname(__file__), path)).expanduser().resolve()
        if os.path.isdir(root):
            try:
                meta = yaml.safe_load(get_file_content(os.path.join(root, 'config.yaml')))
                self.title = meta.get('title', self.title)
                self.vendor = meta.get('vendor', self.vendor)
                self.prefix = meta.get('prefix', self.title.lower())
            except Exception as e:
                print(e)

            for name in os.listdir(root):
                if name.startswith('logo.'):
                    self.logo = os.path.join(root, name)

                if name.startswith('title.'):
                    self.title = get_file_content(os.path.join(root, name))

    ''' 通配符替换'''

    def replace(self, content):

        return content


if __name__ == '__main__':
    config = Config(sys.argv[1])
    print(config.logo)
