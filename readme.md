# MoonCake数据解析

# **注意⚠️**
对代码开发请先切换分支！！！

## 开发环境
> Window、Linux、OSx、Python3.6+

## 部署环境
> Ubuntu、CentOs

## 环境配置
```shell
# 下载python包
pip install -r requirements.txt

# 配置环境变量(根据本机数据库配置)
echo MONGO_HOST=127.0.0.1 >> .env
echo MONGO_PORT=27017 >> .env
echo MONGO_DB=Spider >> .env
echo MONGO_COLL=treasure >> .env
echo MONGO_USER=admin >> .env
echo MONGO_PSW=123456 >> .env
```

## 测试
> 文件内启动: main.py
> 
> 命令行启动: python main.py

## 文件介绍
> conf ———— 配置文件
> 
> dataset  ———— 待解析文件
> 
> logic   ———— 解析逻辑
> 
> modules   ———— 预留，拥挤配置结构化数据库模型
> 
> pattern  ———— 正则语法
> 
> utils.py   ———— 一些小工具
