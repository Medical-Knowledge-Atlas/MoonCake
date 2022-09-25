import json
import re
import os.path
from functools import wraps

from typing import List

from logic.filter import Filter
from utils.db_utils import MongoDriver
from utils.file_utils import read_files


class Parsing:
    def __init__(self, f_type='file', *args, **kwargs):
        self.f_type = f_type
        self.args = args
        self.kwargs = kwargs

    def load_data(self):
        """
        从不同数据源加载待解析数据
        """
        if self.f_type == 'file':
            print('从文件中加载测试数据，文件路径: ./dataset')
            if not os.path.exists('./dataset'):
                print(os.getcwd())
                print('不存在该文件...')
                return []
            for data in read_files('./dataset'):
                for content in json.loads(data)['RECORDS']:
                    yield content
        elif self.f_type == 'm_db':
            print('从MongoDB中加载测试数据...')
            for data in MongoDriver(*self.args, **self.kwargs).get_data():
                yield data
        elif self.f_type == 'pg_db':
            """预留"""
            print('从PG中加载测试数据...')
            return []
        else:
            return []

    @staticmethod
    def load_regulation(path):
        """
        加载解析规则
        """
        if not path:
            return ''
        with open(f'./pattern/{path}', 'r') as f:
            regulations = f.readlines()
        return regulations


def load_test(function):
    @wraps(function)
    def wrap_fun(*args, **kwargs):
        parsing = Parsing()
        if not args and not kwargs:
            print('未输入参数，加载测试数据...')
            text = ''
            for data in parsing.load_data():
                text = data['mainbody']
                if not text:
                    continue
                else:
                    print('加载测试数据         成功')
                    break
            print('加载测试匹配逻辑...')
            patterns = parsing.load_regulation('supplier.txt')
            print('加载测试匹配逻辑        成功')
            return function(text, patterns)
        return function(*args, **kwargs)

    return wrap_fun


@load_test
def parse_entity(data: dict = '', patterns: List = [], filter_name: str = None, is_re=True) -> list:
    """
    从正文中解析出供应商名称
    :param filter_name: 第二层解析函数的名称/解析字段的名称/解析字段规则文件名称
    :param patterns: 匹配模式
    :param data: 待解析字段所在的字典，包含title，time，mainbody等
    :return: 匹配结果
    """
    text = data['mainbody']
    entities = []
    if is_re:
        if not any([text, patterns]):
            print('缺少正文/匹配模式,匹配结束')
            return entities
        for pattern in patterns:
            ret = re.findall(pattern.strip(), text.strip())
            if not ret:
                continue
            entities.append(ret[0].strip())
    else:
        entities = text
    fun = getattr(Filter(), filter_name)
    entities = fun(entities, data) if fun else entities
    return entities


if __name__ == '__main__':
    data = parse_entity()
    print(data)
