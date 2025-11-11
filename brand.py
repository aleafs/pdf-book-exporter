#!/usr/bin/env python3

import os
import pathlib
import sys

import yaml


def get_file_content(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()


class Config:
    title: str = None
    prefix: str = None
    vendor: str = None
    logo: str = None

    def __init__(self, path: str):
        root = pathlib.Path(os.path.join(os.path.dirname(__file__), path)).expanduser().resolve()
        if os.path.isdir(root):
            try:
                meta = yaml.safe_load(get_file_content(os.path.join(root, 'config.yaml')))
                self.title = meta.get('title', self.title)
                self.vendor = meta.get('vendor', self.vendor)
            except Exception as e:
                pass

            for name in os.listdir(root):
                if not self.logo and name.startswith('logo.'):
                    self.logo = os.path.join(root, name)

                if not self.title and name.startswith('title.'):
                    self.title = get_file_content(os.path.join(root, name))

            if not self.title:
                self.title = 'Bluepipe'

            if not self.prefix:
                self.prefix = self.title.lower()

            if not self.vendor:
                self.vendor = '杭州萃蓝网络科技有限公司'

    def __str__(self):
        return f"{self.title}: prefix={self.prefix}, vendor={self.vendor}, logo={self.logo}"

    ''' 通配符替换'''

    def replace(self, content: str):
        return (content.replace('$Brand.Title$', self.title)
                .replace('$Brand.Prefix$', self.prefix)
                .replace('$Brand.Vendor$', self.vendor))


if __name__ == '__main__':
    config = Config(sys.argv[1])
    print(config)
