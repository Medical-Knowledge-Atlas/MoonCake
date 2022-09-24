"""

"""
import os

from utils.db_utils import MongoDriver
from utils.parsing import Parsing, parse_entity


class Gripper:
    """
    拉取、分发数据
    """

    def __init__(self, f_type='file', path=None, db=None, col=None, hots=None, port=None):
        self.parsing = Parsing(f_type, path, db, col, hots, port)
        self.regulation_paths = os.listdir('./pattern')
        self.db = MongoDriver(db, col, hots, port)

    def start(self, regulation_path=None, end_count=10):
        count = 0
        success = 0
        fail = 0
        for data in self.parsing.load_data():
            print('===' * 20, f'\n拉取数据成功，开始解析...')
            self.regulation_paths = self.regulation_paths if not regulation_path else [regulation_path]
            print(f'解析正文: {data["mainbody"]}')
            # todo: 将当前解析数据缓存如redis
            for path in self.regulation_paths:
                regulations = self.parsing.load_regulation(path)
                colum_name = path.split('.')[0]
                entity = parse_entity(data['mainbody'], regulations, colum_name)
                if entity:
                    print('解析成功')
                    success += 1
                    data[colum_name] = entity
                    print(f'增则解析结果: {entity}')
                else:
                    fail += 1
                    print('解析失败')
            self.save(data)
            count += 1
            print('===' * 20)
            if end_count == count:
                print(f'解析结束: \n总记录数: {count} \n成功数: {success} \n失败数: {fail}\n成功率: {(success / count) * 100:.2f}%')
                return []

    def save(self, data):
        print('存储记录')
        self.db.save_data(data)
