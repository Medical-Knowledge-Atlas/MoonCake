from typing import Union
import re
import os

from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
from logic.gripper import Gripper

if __name__ == '__main__':
    # text = "招标时间：2021年08月20日 　　项目名称：CO2超脉冲点阵激光 　　中标公司：南京慧加鑫医疗科技有限公司 　　中标品牌：科英激光 　　公示时间：2022年01月18日—2022年01月21日"
    # pattern = '.*[中标公司|中标|公司][：|:| ](\w+ ).*'
    # data = re.findall(pattern, text)[0]
    # print(data)
    for data in Gripper(f_type='file').start():
        if data:
            print(data)
        else:
            print('')