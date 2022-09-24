from os import getenv
from dotenv import load_dotenv

load_dotenv()


# 数据库配置
MONGO_HOST: str = getenv('MONGO_HOST', '127.0.0.1')
MONGO_PORT: str = getenv('MONGO_PORT', 27017)
MONGO_DB: str = getenv('MONGO_DB', 'Spider')
MONGO_COLL: str = getenv('MONGO_COLL', 'treasure')
MONGO_USER: str = getenv('MONGO_USER', 'admin')
MONGO_PSW: str = getenv('MONGO_PSW', '123456')