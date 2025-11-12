#!/usr/bin/env python3

import os
import pathlib
import sys

import yaml


def get_file_content(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()


def load_brand_config(path: str):
    that = Config()
    root = pathlib.Path(os.path.join(os.path.dirname(__file__), path)).expanduser().resolve()
    if os.path.isdir(root):
        try:
            meta = yaml.safe_load(get_file_content(os.path.join(root, 'config.yaml')))
            that.title = meta.get('title', that.title)
            that.vendor = meta.get('vendor', that.vendor)
        except Exception as e:
            pass

        for name in os.listdir(root):
            if not that.logo and name.startswith('logo.'):
                that.logo = os.path.join(root, name)

            if not that.title and name.startswith('title.'):
                that.title = get_file_content(os.path.join(root, name))

        if not that.title:
            that.title = 'Bluepipe'

        if not that.prefix:
            that.prefix = that.title.lower()

        if not that.vendor:
            that.vendor = '杭州萃蓝网络科技有限公司'

    return that


class Config:
    title: str = None
    prefix: str = None
    vendor: str = None
    logo: str = None

    def __str__(self):
        return f"{self.title}: prefix={self.prefix}, vendor={self.vendor}, logo={self.logo}"

    ''' 通配符替换'''

    def replace(self, content: str):
        return (content.replace('$Title$', self.title)
                .replace('$Prefix$', self.prefix)
                .replace('$Vendor$', self.vendor))


if __name__ == '__main__':
    config = load_brand_config(sys.argv[1])
    print(config)
